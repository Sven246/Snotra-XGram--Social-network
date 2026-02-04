from app.extensions import db
from app.core.models.ad import Ad

class AdsService:

    @staticmethod
    def create(title, image_url=None, link=None):
        ad = Ad(
            title=title,
            image_url=image_url,
            link=link
        )
        db.session.add(ad)
        db.session.commit()
        return ad

    @staticmethod
    def get_active_ads():
        return Ad.query.filter_by(is_active=True).all()

    @staticmethod
    def get_single_ad():
        return Ad.query.filter_by(is_active=True).order_by(Ad.created_at.desc()).first()
