import logging

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


LOGGER = logging.getLogger(__name__)

db = SQLAlchemy()


def create_app(
    name: str = __name__,
    **settings: dict
) -> Flask:
    """Retorna uma instancia do Flask"""
    from . import config, carros

    print('Iniciando %s %s', config.APP_NAME, config.APP_VERSION)

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config ['JSON_SORT_KEYS'] = False

    @app.before_first_request
    def cria_banco():
        db.create_all()

    if not settings:  # Utiliza a configuracao padrao, caso nao seja passada
        app.config.from_object(config)

    if settings:  # Utiliza a configuracao passada
        app.config.from_mapping(settings)
    print('Configurado Flask')

    db.init_app(app)
    print('Configurado Flask SQLAlchemy')

    CORS(app)
    print('Configurado Flask CORS')

    app.register_blueprint(carros.app)

    return app
