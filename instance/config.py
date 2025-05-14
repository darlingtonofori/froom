# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://forum_db_e89m_user:ZyAxYHd3eSU8AHDbjTh591yYAO6hjs4X@dpg-d0hpuae3jp1c73bscca0-a/forum_db_e89m'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
