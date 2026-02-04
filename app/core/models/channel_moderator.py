from app.extensions import db

class ChannelModerator(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    channel_id = db.Column(db.Integer, db.ForeignKey("channel.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # права модератора
    can_post = db.Column(db.Boolean, default=True)
    can_delete = db.Column(db.Boolean, default=True)
    can_ban = db.Column(db.Boolean, default=True)
