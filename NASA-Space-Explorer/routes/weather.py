from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_space_weather
from datetime import datetime, timedelta

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/')
def index():
    today = datetime.now()
    default_start = (today - timedelta(days=30)).strftime('%Y-%m-%d')
    
    start_date = request.args.get('start_date', default_start)
    end_date = request.args.get('end_date', today.strftime('%Y-%m-%d'))
    
    weather_data = fetch_space_weather(start_date=start_date, end_date=end_date)
    
    # NASA DONKI API returns string 'None' when an API error/503 occurs and we swallow it.
    # We should make sure weather_data actually contains lists to avoid len() errors in Jinja.
    if not isinstance(weather_data.get('flares'), list): weather_data['flares'] = []
    if not isinstance(weather_data.get('storms'), list): weather_data['storms'] = []
    if not isinstance(weather_data.get('cmes'), list): weather_data['cmes'] = []
    if not isinstance(weather_data.get('notifications'), list): weather_data['notifications'] = []
    
    return render_template('weather.html', 
                           data=weather_data, 
                           start_date=start_date,
                           end_date=end_date)
