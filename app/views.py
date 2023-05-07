from flask import Blueprint, render_template
from flask_login import login_required, current_user

# define routes
views = Blueprint('views', __name__)

# @views.route('/')
# @login_required
# def home():
#     return render_template('home.html', user=current_user)

@views.route('/article')
@login_required
def article():
    return render_template('article.html', user=current_user)

@views.route('/document')
@login_required
def document():
    return render_template('document.html', user=current_user)