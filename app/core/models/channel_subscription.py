from app.extensions import db
from datetime import datetime

class ChannelSubscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    channel_id = db.Column(db.Integer, db.ForeignKey("channel.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # скрыть подписку от других
    hidden = db.Column(db.Boolean, default=False)
