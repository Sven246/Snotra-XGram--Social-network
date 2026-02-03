from app.extensions import db
from datetime import datetime

class CoinTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    amount = db.Column(db.Integer)
    type = db.Column(db.String(50))
    description = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
