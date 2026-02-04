from app.extensions import db
from app.core.models.premium_subscription import PremiumSubscription
from datetime import datetime, timedelta

class PremiumService:

    @staticmethod
    def activate(user, days: int, price: int):
        expires = datetime.utcnow() + timedelta(days=days)

        user.is_premium = True
        user.premium_expires_at = expires

        sub = PremiumSubscription(
            user_id=user.id,
            type=f"{days}days",
            price=price,
            expires_at=expires
        )

        db.session.add(sub)
        db.session.commit()

    @staticmethod
    def check_expiration(user):
        if user.is_premium and user.premium_expires_at < datetime.utcnow():
            user.is_premium = False
            db.session.commit()
