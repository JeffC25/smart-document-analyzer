from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .nlp import Content
from .nfi import getArticle

# define routes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('login.html', user=current_user)

@views.route('/article', methods=['GET','POST'])
@login_required
def article():
    if request.method == 'POST':
        print("Analyzing...")
        article=request.form.get('article')
        try:
            content = Content(getArticle(article)[1])
            content.summarize()
            content.getKeywords()
            content.getPolarity()

            for j in content.keywords:
                print(j)

            # return redirect(url_for('views.article_analysis'))
            return render_template('article_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('article.html', user=current_user)

@views.route('/document', methods=['GET', 'POST'])
@login_required
def document():
    return render_template('document.html', user=current_user)

# @views.route('/article-results')
# @login_required
# def article_analysis():
#     return render_template('article_results.html', user=current_user)

# @views.route('/document-results') 
# @login_required
# def document_analysis():
#     return render_template('document_results.html', user=current_user)