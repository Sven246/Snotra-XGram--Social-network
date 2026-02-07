from flask import request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.core.models.comment import Comment

def register(api):
    @api.route("/comments/add", methods=["POST"])
    @login_required
    def add_comment():
        post_id = request.json.get("post_id")
        content = request.json.get("content")

        comment = Comment(
            post_id=post_id,
            user_id=current_user.id,
            content=content
        )
        db.session.add(comment)
        db.session.commit()

        return jsonify({"status": "ok", "comment_id": comment.id})
