from flask_sqlalchemy import SQLAlchemy
from mainapp import db

class Pin(db.Model):
    pkid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    rating1 = db.Column(db.Integer, nullable=False)
    rating2 = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    favorited = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, address, latitude, longitude, rating1, rating2, description, favorited):
        self.title = title
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.rating1 = rating1
        self.rating2 = rating2
        self.description = description
        self.favorited = favorited
