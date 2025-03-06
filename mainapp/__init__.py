from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'pins.db')

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

  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  with app.app_context():
    db.create_all()

  return app