from flask import Blueprint, render_template, request, redirect, url_for
import re

search_bp = Blueprint('search', __name__)

@search_bp.route('/')
def index():
    query = request.args.get('q', '').strip()
    
    if not query:
        return redirect(url_for('main.index'))
        
    # Check if query is a date YYYY-MM-DD
    if re.match(r'^\d{4}-\d{2}-\d{2}$', query):
        return redirect(url_for('apod.index', date=query))
    
    return render_template('search_results.html', query=query)
