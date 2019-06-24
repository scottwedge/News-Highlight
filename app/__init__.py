from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
app = Flask(__name__,instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap.init_app(app)

# Will and the views and forms

return app
# from .main import views
# from .main import errors
