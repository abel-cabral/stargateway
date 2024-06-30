from flask import Flask
from app.config import Config
from app.errors import handlers

def gateway():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Importar as rotas
        from app.routes import api
        app.register_blueprint(api)

        # Configurar manipuladores de erro
        app.register_error_handler(404, handlers.page_not_found)
        app.register_error_handler(500, handlers.internal_server_error)

        return app