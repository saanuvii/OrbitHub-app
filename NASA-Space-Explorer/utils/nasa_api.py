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
        # Even if it's 429, we want the JSON response to read the message
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
            
        # Flatten the structure
        asteroids = []
        for date, neos in data.get('near_earth_objects', {}).items():
            asteroids.extend(neos)
            
        # Sort by closest approach
        asteroids.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['kilometers'])
        return asteroids
    except Exception as e:
        return {'error': True, 'msg': 'Failed to connect to NASA NeoWs API.'}

