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

@pinapp.route('/view_pin', methods=['GET'])
def view_pin():
    pkid = request.args.get('pkid')
    pin = pins_svc.get_pin(pkid)

    print(pin)
    return render_template('viewpin.html', given_pin=pin)

@pinapp.route('/edit_pin', methods=['GET', 'POST'])
def edit_pin():
    pkid = request.args.get('pkid')
    pin = pins_svc.get_pin(pkid)

    return render_template('editpin.html', given_pin=pin)

@pinapp.route('/submit_edited_pin', methods=['POST'])
def submit_edited_pin():
    loc = Nominatim(user_agent='GetLoc')

    pkid = request.args.get('pkid')
    title = request.form.get('title')
    address = request.form.get('address')
    rating1 = request.form.get('rating1')
    rating2 = request.form.get('rating2')
    description = request.form.get('description')

    getLoc = loc.geocode(address)

    pins_svc.edit_pin(pkid, title, address, getLoc.latitude, getLoc.longitude, rating1, rating2, description)
    
    #return redirect(url_for('pins.viewpin?pkid={{ pkid }}'))
    return redirect(url_for('maproute.home'))