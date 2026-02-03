from flask import Blueprint
from . import auth, coins, premium, stories, posts, comments, settings, profile

def register_api_v1(app):
    api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

    auth.register(api_v1)
    coins.register(api_v1)
    premium.register(api_v1)
    stories.register(api_v1)
    posts.register(api_v1)
    comments.register(api_v1)
    settings.register(api_v1)
    profile.register(api_v1)

    app.register_blueprint(api_v1)
