from flask import Blueprint, render_template, request, redirect, url_for

pinapp = Blueprint('pins', __name__, template_folder='templates', static_folder='static')

@pinapp.route('/make_new_pin', methods=['GET'])
def make_new_pin():
    return render_template('newpin.html')

@pinapp.route('/submit_pin', methods=['POST'])
def submit_pin():
    address = request.form.get('address')
    rating1 = request.form.get('rating1')
    rating2 = request.form.get('rating2')
    description = request.form.get('description')

    print(f"New Pin - Address: {address}, Mayah's Rating: {rating1}, Jude's Rating: {rating2}, Description: {description}")

    return redirect(url_for('maproute.home'))
