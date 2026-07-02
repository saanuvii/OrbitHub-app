import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    NASA_API_KEY = os.environ.get('NASA_API_KEY', 'DEMO_KEY')
    
    # Database Setup (Fallback to SQLite if no Supabase URL is provided)
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = database_url or 'sqlite:///' + os.path.join(basedir, 'database', 'favorites.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Caching Setup
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
