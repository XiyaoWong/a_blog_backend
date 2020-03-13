from flask import Flask
from flask_cors import  CORS

from app.config import Config
from app.api import api_bp


def create_app() -> Flask:
    app = Flask(__name__)

    configure_app(app)
    configure_blueprints(app)
    if app.config.get("CORS") == True:
        CORS(app)
    print(app.url_map)
    return app


def configure_app(app: Flask):
    app.config.from_object(Config)


def configure_blueprints(app: Flask):
    app.register_blueprint(api_bp, url_prefix="")
