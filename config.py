import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')

    # Fix for Render PostgreSQL URL format
    db_url = os.environ.get('DATABASE_URL', 'sqlite:///jobboard.db')
    if db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'static', 'resumes')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024