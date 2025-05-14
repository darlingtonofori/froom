import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
