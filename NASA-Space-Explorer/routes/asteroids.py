from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_asteroids
from datetime import datetime, timedelta
import json

asteroids_bp = Blueprint('asteroids', __name__)

@asteroids_bp.route('/')
def index():
    today = datetime.now()
    start_date = request.args.get('start_date', today.strftime('%Y-%m-%d'))
    
    # NASA API restricts range to 7 days
    try:
        start_obj = datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        start_obj = today
        start_date = today.strftime('%Y-%m-%d')
        
    end_obj = start_obj + timedelta(days=7)
    end_date = end_obj.strftime('%Y-%m-%d')
    
    asteroids = fetch_asteroids(start_date=start_date, end_date=end_date)
    
    # Pre-process payloads for frontend
    for ast in asteroids:
        ast['fav_payload'] = json.dumps({
            'item_type': 'asteroid',
            'title': ast['name'],
            'image_url': '',
            'id': ast['id'],
            'is_potentially_hazardous_asteroid': ast['is_potentially_hazardous_asteroid'],
            'close_approach_date': ast['close_approach_data'][0]['close_approach_date'],
            'miss_distance': ast['close_approach_data'][0]['miss_distance']['kilometers']
        }).replace('"', '&quot;')
        
    return render_template('asteroids.html', 
                           asteroids=asteroids, 
                           start_date=start_date)
