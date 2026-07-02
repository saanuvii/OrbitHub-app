from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_epic

epic_bp = Blueprint('epic', __name__)

@epic_bp.route('/')
def index():
    date = request.args.get('date')
    epic_data = fetch_epic(date)
    
    return render_template('epic.html', data=epic_data, selected_date=date)
