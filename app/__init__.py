from flask import Flask
from app.config import Config
from app.errors import handlers
from app.routers.websage import api as websage_api

def gateway():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        app.register_blueprint(websage_api)

        # Configurar manipuladores de erro
        app.register_error_handler(404, handlers.page_not_found)
        app.register_error_handler(500, handlers.internal_server_error)

        return app