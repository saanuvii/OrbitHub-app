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
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching APOD: {e}")
        return None

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
        response.raise_for_status()
        data = response.json()
        
        # Flatten the structure
        asteroids = []
        for date, neos in data.get('near_earth_objects', {}).items():
            asteroids.extend(neos)
            
        # Sort by closest approach
        asteroids.sort(key=lambda x: x['close_approach_data'][0]['miss_distance']['kilometers'])
        return asteroids
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Asteroids: {e}")
        return []

def fetch_space_weather(start_date=None, end_date=None):
    if not start_date:
        start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    
    api_key = get_api_key()
    weather_data = {
        "flares": [],
        "storms": [],
        "cmes": [],
        "notifications": []
    }
    
    try:
        # Fetch Solar Flares
        flares_url = "https://api.nasa.gov/DONKI/FLR"
        params = {"startDate": start_date, "api_key": api_key}
        if end_date: params["endDate"] = end_date
        flares_res = requests.get(flares_url, params=params, timeout=10)
        if flares_res.status_code == 200:
            weather_data["flares"] = flares_res.json()
            
        # Fetch Geomagnetic Storms
        storms_url = "https://api.nasa.gov/DONKI/GST"
        storms_res = requests.get(storms_url, params=params, timeout=10)
        if storms_res.status_code == 200:
            weather_data["storms"] = storms_res.json()
            
        # Fetch CMEs
        cmes_url = "https://api.nasa.gov/DONKI/CME"
        cmes_res = requests.get(cmes_url, params=params, timeout=10)
        if cmes_res.status_code == 200:
            weather_data["cmes"] = cmes_res.json()
            
        # Fetch Notifications
        notif_url = "https://api.nasa.gov/DONKI/notifications"
        notif_params = {"startDate": start_date, "type": "all", "api_key": api_key}
        if end_date: notif_params["endDate"] = end_date
        notif_res = requests.get(notif_url, params=notif_params, timeout=10)
        if notif_res.status_code == 200:
            weather_data["notifications"] = notif_res.json()
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Space Weather: {e}")
        
    return weather_data
