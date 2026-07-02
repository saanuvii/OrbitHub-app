import requests
import os
from config import Config
from flask import current_app
from datetime import datetime, timedelta

def get_api_key():
    return current_app.config.get('NASA_API_KEY', 'DEMO_KEY')

def fetch_apod(date=None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": get_api_key()}
    if date:
        params["date"] = date
        
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if response.status_code != 200:
            return {'error': True, 'msg': data.get('msg') or data.get('error', {}).get('message', 'NASA API Error')}
        return data
    except Exception as e:
        return {'error': True, 'msg': 'Failed to connect to NASA APOD API.'}

def fetch_asteroids(start_date=None, end_date=None):
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")
    if not end_date:
        end_date = start_date
        
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": get_api_key()
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        
        if response.status_code != 200:
            return {'error': True, 'msg': data.get('error_message') or data.get('error', {}).get('message', 'NASA API Error')}
            
        asteroids = []
        for date, neos in data.get('near_earth_objects', {}).items():
            asteroids.extend(neos)
            
        asteroids.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['kilometers'])
        return asteroids
    except Exception as e:
        return {'error': True, 'msg': 'Failed to connect to NASA NeoWs API.'}

def fetch_epic(date=None):
    api_key = get_api_key()
    
    # If no date, get the most recent date available first
    if not date:
        try:
            latest_url = f"https://api.nasa.gov/EPIC/api/natural/all?api_key={api_key}"
            response = requests.get(latest_url, timeout=10)
            if response.status_code == 200 and len(response.json()) > 0:
                date = response.json()[0]['date']
            else:
                return {'error': True, 'msg': 'Could not fetch recent EPIC dates.'}
        except Exception:
             return {'error': True, 'msg': 'Failed to connect to NASA EPIC API.'}
             
    # Fetch images for the specific date
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if response.status_code != 200:
            return {'error': True, 'msg': data.get('msg') or data.get('error', {}).get('message', 'NASA API Error')}
            
        # Format the data to include direct image URLs
        # EPIC URL format: https://api.nasa.gov/EPIC/archive/natural/YYYY/MM/DD/png/epic_1b_20151031074844.png?api_key=DEMO_KEY
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%Y/%m/%d')
        
        for item in data:
            item['image_url'] = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{item['image']}.png?api_key={api_key}"
            
        return {'date': date, 'images': data}
    except Exception as e:
        return {'error': True, 'msg': 'Failed to fetch EPIC imagery.'}

def fetch_exoplanets():
    # NASA Exoplanet Archive uses a TAP (Table Access Protocol) API
    # We will query a subset of confirmed planets for performance.
    # We don't need an API key for this specific open endpoint.
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    
    # Simple query: Get 50 interesting exoplanets with basic details
    # pl_name (Name), hostname (Star), pl_bmasse (Earth Mass), pl_rade (Earth Radius), disc_year (Discovery Year), discoverymethod
    query = """
    select top 100 pl_name, hostname, discoverymethod, disc_year, pl_bmasse, pl_rade, sy_dist 
    from pscomppars 
    where pl_bmasse is not null and sy_dist is not null
    order by disc_year desc, sy_dist asc
    """
    
    params = {
        "query": query,
        "format": "json"
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        if response.status_code != 200:
            return {'error': True, 'msg': 'NASA Exoplanet Archive is currently unavailable.'}
        return response.json()
    except Exception as e:
        return {'error': True, 'msg': 'Failed to connect to Exoplanet API.'}
