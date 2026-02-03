from app.extensions import db
from datetime import datetime

class PremiumSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    type = db.Column(db.String(50))  # month, 90days, halfyear, year
    price = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)
