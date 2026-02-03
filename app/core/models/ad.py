from app.extensions import db
from datetime import datetime

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    link = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    is_active = db.Column(db.Boolean, default=True)
    show_in_channels = db.Column(db.Boolean, default=True)
