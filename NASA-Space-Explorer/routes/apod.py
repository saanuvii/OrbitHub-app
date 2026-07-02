from flask import Blueprint, render_template, request
from utils.nasa_api import fetch_apod

apod_bp = Blueprint('apod', __name__)

@apod_bp.route('/')
def index():
    date = request.args.get('date')
    data = fetch_apod(date)
    return render_template('apod.html', data=data)
