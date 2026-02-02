from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager
from .api.v1 import register_api_v1
from .web import register_web_blueprints

def create_app():
  app = Flask(__name__)
  app.comfig.from_object(Config)

# init extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app, db)

# register API
register_api_v1(app)

  # register web routes
register_web_blueprints(app)

return app
