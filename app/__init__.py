from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
  app = Flask(__name__)

  app.config.from_object(config_options[config_name])


# Initializing Flask Extensions
  bootstrap.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  # Will and the views and forms
  from .request import configure_request
  configure_request(app)

  return app
# from .main import views
# from .main import errors
