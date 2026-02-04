from app.extensions import db
from app.core.models.channel import Channel
from app.core.models.channel_post import ChannelPost
from app.core.models.channel_subscription import ChannelSubscription
from app.core.models.channel_moderator import ChannelModerator
from app.core.models.channel_reaction import ChannelReaction
from app.core.models.channel_analytics import ChannelAnalytics
from datetime import datetime

class ChannelsService:

    # --- CHANNELS ---
    @staticmethod
    def create_channel(owner, title, description, type="public"):
        channel = Channel(
            owner_id=owner.id,
            title=title,
            description=description,
            type=type
        )
        db.session.add(channel)
        db.session.commit()
        return channel

    @staticmethod
    def subscribe(user, channel):
        if ChannelsService.is_subscribed(user, channel):
            return

        sub = ChannelSubscription(
            user_id=user.id,
            channel_id=channel.id
        )
        db.session.add(sub)
        db.session.commit()

    @staticmethod
    def is_subscribed(user, channel):
        return ChannelSubscription.query.filter_by(
            user_id=user.id,
            channel_id=channel.id
        ).first() is not None

    # --- POSTS ---
    @staticmethod
    def create_post(channel, author, content, media_url=None):
        post = ChannelPost(
            channel_id=channel.id,
            author_id=author.id,
            content=content,
            media_url=media_url
        )
        db.session.add(post)
        db.session.commit()
        return post

    # --- REACTIONS ---
    @staticmethod
    def add_reaction(user, post, emoji):
        reaction = ChannelReaction(
            user_id=user.id,
            post_id=post.id,
            emoji=emoji
        )
        db.session.add(reaction)
        db.session.commit()

    # --- ANALYTICS ---
    @staticmethod
    def add_view(user, post):
        view = ChannelAnalytics(
            user_id=user.id,
            post_id=post.id,
            channel_id=post.channel_id,
            viewed_at=datetime.utcnow()
        )
        db.session.add(view)
        db.session.commit()
