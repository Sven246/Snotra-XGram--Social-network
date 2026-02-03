from flask import Blueprint

# Импортируем модули API
from . import auth
from . import ads

def register_api_v1(app):
    api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

    # Регистрация маршрутов
    auth.register(api_v1)
    ads.register(api_v1)

    app.register_blueprint(api_v1)
