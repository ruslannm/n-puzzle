from flask import Flask
# from flask_bootstrap import Bootstrap
from config_web import Config

# bootstrap = Bootstrap()

app = Flask(__name__)
app.config.from_object(Config)
# bootstrap.init_app(app)

from app import routes