from app import app, db  # Make sure db is imported here
from app import models   # Make sure this imports your models so SQLAlchemy sees them

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ Auto-create tables if they don't exist
    app.run(debug=True)
