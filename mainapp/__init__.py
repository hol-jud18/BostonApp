from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app=Flask( __name__, 
            template_folder='templates', 
            static_folder='static', 
            static_url_path='' )
  

  from .routes.map.maproute import mapapp as map_blueprint
  from .routes.pins.pinsroute import pinapp as pin_blueprint

  app.register_blueprint(map_blueprint, url_prefix='/map')
  app.register_blueprint(pin_blueprint, url_prefix='/pin')

  return app