from flask import request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.core.models.ad import Ad

def register(api):
    @api.route("/ads/create", methods=["POST"])
    @login_required
    def create_ad():
        if not current_user.is_admin:
            return jsonify({"error": "Forbidden"}), 403

        data = request.json
        ad = Ad(
            title=data.get("title"),
            image_url=data.get("image_url"),
            link=data.get("link")
        )
        db.session.add(ad)
        db.session.commit()

        return jsonify({"status": "ok", "ad_id": ad.id})
