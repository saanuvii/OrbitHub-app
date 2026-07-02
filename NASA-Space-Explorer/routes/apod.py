from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_apod
import json

apod_bp = Blueprint('apod', __name__)

@apod_bp.route('/')
def index():
    date = request.args.get('date')
    data = fetch_apod(date)
    
    # Check if we have valid data and format payload for favorites
    payload = None
    if data and 'title' in data:
        # Create a payload for the favorites button
        payload = json.dumps({
            'item_type': 'apod',
            'title': data.get('title'),
            'image_url': data.get('url') if data.get('media_type') == 'image' else data.get('thumbnail_url', ''),
            'date': data.get('date'),
            'explanation': data.get('explanation')
        }).replace('"', '&quot;')
        
    return render_template('apod.html', data=data, payload=payload)
