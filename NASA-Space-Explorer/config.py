import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    NASA_API_KEY = os.environ.get('NASA_API_KEY', 'DEMO_KEY')
    
    # Caching Setup
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
