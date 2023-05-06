from flask import Blueprint, render_template

# define routes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')