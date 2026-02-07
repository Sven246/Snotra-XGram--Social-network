from flask import request, jsonify
from flask_login import login_required, current_user
from app.core.services.story_service import StoryService

def register(api):
    @api.route("/stories/create", methods=["POST"])
    @login_required
    def create_story():
        media_url = request.json.get("media_url")

        if not current_user.is_premium:
            return jsonify({"error": "Premium only"}), 403

        story = StoryService.create_story(current_user, media_url)
        return jsonify({"status": "ok", "story_id": story.id})

    @api.route("/stories/<int:user_id>")
    @login_required
    def get_stories(user_id):
        stories = StoryService.get_active_stories(user_id)
        return jsonify([
            {"id": s.id, "media_url": s.media_url}
            for s in stories
        ])
