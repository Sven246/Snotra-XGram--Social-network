from app.extensions import db
from app.core.models.story import Story
from datetime import datetime, timedelta

class StoryService:

    @staticmethod
    def create_story(user, media_url):
        story = Story(
            user_id=user.id,
            media_url=media_url,
            expires_at=datetime.utcnow() + timedelta(hours=24)
        )
        db.session.add(story)
        db.session.commit()
        return story

    @staticmethod
    def get_active_stories(user_id):
        now = datetime.utcnow()
        return Story.query.filter(
            Story.user_id == user_id,
            Story.expires_at > now
        ).all()
