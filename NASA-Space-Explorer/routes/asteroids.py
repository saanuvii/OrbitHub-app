from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_asteroids
from datetime import datetime, timedelta

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
        
    return render_template('asteroids.html', 
                           asteroids=asteroids, 
                           start_date=start_date)
