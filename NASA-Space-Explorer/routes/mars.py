from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_mars_photos
import json

mars_bp = Blueprint('mars', __name__)

@mars_bp.route('/')
def index():
    rover = request.args.get('rover', 'curiosity')
    date = request.args.get('date', '')
    camera = request.args.get('camera', 'all')
    page = request.args.get('page', 1, type=int)
    
    photos = fetch_mars_photos(rover=rover, earth_date=date if date else None, camera=camera, page=page)
    
    # Pre-process payloads for frontend
    for photo in photos:
        photo['fav_payload'] = json.dumps({
            'item_type': 'mars',
            'title': f"{photo['rover']['name']} - {photo['camera']['name']} (Sol {photo['sol']})",
            'image_url': photo['img_src'],
            'rover': photo['rover']['name'],
            'camera': photo['camera']['full_name'],
            'earth_date': photo['earth_date']
        }).replace('"', '&quot;')
    
    return render_template('mars.html', 
                           photos=photos, 
                           rover=rover, 
                           date=date, 
                           camera=camera,
                           page=page)
