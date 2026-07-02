from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(50), nullable=False) # e.g., 'apod', 'mars', 'asteroid'
    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(500))
    data = db.Column(db.Text) # JSON string to store all other details
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_data(self, data_dict):
        self.data = json.dumps(data_dict)

    def get_data(self):
        return json.loads(self.data) if self.data else {}
