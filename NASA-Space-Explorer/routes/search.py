from flask import Blueprint, render_template, request, redirect, url_for

search_bp = Blueprint('search', __name__)

@search_bp.route('/')
def index():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', 'all')
    
    if not query:
        return redirect(url_for('main.index'))
        
    # Since we can't globally search all NASA APIs with one keyword easily,
    # we'll implement a routing mechanism based on the category.
    # For a real global search, we'd need a local indexed database of fetched content.
    
    # For now, let's redirect to specific pages based on what looks like a date or name
    
    import re
    # Check if query is a date YYYY-MM-DD
    if re.match(r'^\d{4}-\d{2}-\d{2}$', query):
        if category == 'apod' or category == 'all':
            return redirect(url_for('apod.index', date=query))
        elif category == 'mars':
            return redirect(url_for('mars.index', date=query))
    
    # Check if query looks like a rover name
    rovers = ['curiosity', 'opportunity', 'spirit', 'perseverance']
    if query.lower() in rovers:
        return redirect(url_for('mars.index', rover=query.lower()))
        
    # Default fallback: redirect to asteroids page (it doesn't have name search, but we can send them there)
    # Ideally, we would render a search results page here if we had local search capabilities
    
    return render_template('search_results.html', query=query, category=category)
