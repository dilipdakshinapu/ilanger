import os
from flask import Flask
from konfig import Config
from flask_sqlalchemy import SQLAlchemy

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
SETTINGS = os.path.join(BASE_PATH, 'settings.ini')

db = SQLAlchemy()

def create_app():
    """
    Create the app object and return it
    """
    app = Flask(__name__)

    # Load application settings
    settings = os.environ.get("FLASK_SETTINGS", SETTINGS)
    if settings is not None:
        c = Config(settings)
        print(c)
        app.config.update(c.get_map('flask'))

    from users.views import user
    # Register the blueprints to app
    app.register_blueprint(user)

    db.init_app(app)

    return app


