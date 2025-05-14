from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://forum_db_e89m_user:ZyAxYHd3eSU8AHDbjTh591yYAO6hjs4X@dpg-d0hpuae3jp1c73bscca0-a/forum_db_e89m'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

from app import routes
