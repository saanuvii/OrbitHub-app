from flask import Blueprint, render_template
from utils.nasa_api import fetch_exoplanets

exoplanets_bp = Blueprint('exoplanets', __name__)

@exoplanets_bp.route('/')
def index():
    data = fetch_exoplanets()
    return render_template('exoplanets.html', data=data)
