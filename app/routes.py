from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/services')
def services():
    return render_template('services.html') 

@main.route('/team')
def team():
    return render_template('team.html')

@main.route('/book')
def book():
    return render_template('book.html')