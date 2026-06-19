from flask import Flask
from .routes.main import main_bp


def create_app(config_object="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
