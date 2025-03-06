from flask import Blueprint, render_template, request, redirect, url_for
from geopy.geocoders import Nominatim
from mainapp import db
from mainapp.database import Pin
from mainapp.services import pins_svc

pinapp = Blueprint('pins', __name__, template_folder='templates', static_folder='static')

@pinapp.route('/make_new_pin', methods=['GET'])
def make_new_pin():
    return render_template('newpin.html')

@pinapp.route('/submit_pin', methods=['POST'])
def submit_pin():
    loc = Nominatim(user_agent='GetLoc')

    title = request.form.get('title')
    address = request.form.get('address')
    rating1 = request.form.get('rating1')
    rating2 = request.form.get('rating2')
    description = request.form.get('description')

    getLoc = loc.geocode(address)

    pins_svc.add_new_pin(title, address, getLoc.latitude, getLoc.longitude, rating1, rating2, description)

    print(f"Saved Pin - Latitude: {getLoc.latitude}, Longitude: {getLoc.longitude}, Mayah's Rating: {rating1}, Jude's Rating: {rating2}, Description: {description}")
    
    return redirect(url_for('maproute.home'))
