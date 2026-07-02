from flask import Blueprint, render_template, request, jsonify
from database.models import db, Favorite
import json

favorites_bp = Blueprint('favorites', __name__)

@favorites_bp.route('/')
def index():
    favorites = Favorite.query.order_by(Favorite.created_at.desc()).all()
    
    # Process favorites based on type to easily render them
    processed_favs = []
    for fav in favorites:
        fav_data = fav.get_data()
        processed_favs.append({
            'id': fav.id,
            'type': fav.item_type,
            'title': fav.title,
            'image_url': fav.image_url,
            'date': fav.created_at.strftime("%Y-%m-%d %H:%M"),
            'details': fav_data
        })
        
    return render_template('favorites.html', favorites=processed_favs)

@favorites_bp.route('/add', methods=['POST'])
def add_favorite():
    try:
        data = request.json
        if not data or 'item_type' not in data or 'title' not in data:
            return jsonify({'success': False, 'message': 'Invalid data provided'}), 400
            
        # Check if already exists (basic check based on title and type)
        existing = Favorite.query.filter_by(
            item_type=data['item_type'], 
            title=data['title']
        ).first()
        
        if existing:
            return jsonify({'success': False, 'message': 'Already in favorites'})
            
        new_fav = Favorite(
            item_type=data['item_type'],
            title=data['title'],
            image_url=data.get('image_url', '')
        )
        
        # Remove core fields from data before saving as JSON payload
        details = {k: v for k, v in data.items() if k not in ['item_type', 'title', 'image_url']}
        new_fav.set_data(details)
        
        db.session.add(new_fav)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Added to favorites'})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@favorites_bp.route('/remove/<int:id>', methods=['POST'])
def remove_favorite(id):
    try:
        fav = Favorite.query.get_or_404(id)
        db.session.delete(fav)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500
