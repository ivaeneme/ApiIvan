from flask import Flask
from app.routes import menu
from app.utils.db import init_app

def crear_app():
    app = Flask(__name__)
    app.config.from_object(('app.configs.ConfigDB'))

    init_app(app)
    app.register_blueprint(menu.bp)
    return app