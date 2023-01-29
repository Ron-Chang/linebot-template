from importlib import import_module

from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from rejson import Client

from config import Config
from handlers.error_handler import error_bp

app = Flask(__name__)

app.config.from_object(Config)
CORS(app, send_wildcard=True)  # 允許跨域請求
Compress(app)  # 壓縮


def _init_services():
    from services.linebot_service import LinebotService
    app.linebot = LinebotService(
        access_token=Config.LINEBOT_ACCESS_TOKEN,
        secret=Config.LINEBOT_SECRET,
    )


def _init_database():
    app.rs = Client(
        host=Config.RS_HOST,
        port=Config.RS_PORT,
        charset='utf-8',
        decode_responses=True,
    )


def _init_controllers():
    modules = [
        'controllers.features',
    ]
    if Config.STAGE in {'dev', 'uat'}:
        modules.append('controllers.developments')
    for module in modules:
        import_module(module)


def _register_error_handling():
    app.register_blueprint(error_bp)


def create_app():
    _init_services()
    _init_database()
    _init_controllers()
    _register_error_handling()
    return app
