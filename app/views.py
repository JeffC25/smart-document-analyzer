from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import File, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .nlp import Content
from .nfi import getArticle
from .sfu import uploadFile
import logging

logging.basicConfig(level=logging.INFO, format="(%(asctime)s): %(message)s")

# define routes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.article'))
    else:
        return redirect(url_for('auth.login'))


@views.route('/article', methods=['GET','POST'])
@login_required
def article():
    if request.method == 'POST':
        logging.info("Analyzing...")
        article=request.form.get('article')
        try:
            content = Content(getArticle(article)[1])
            content.summarize()
            content.getKeywords()
            content.getPolarity()

            return render_template('article_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('article.html', user=current_user)


@views.route('/document', methods=['GET', 'POST'])
@login_required
def document():
    if request.method == 'POST':
        logging.info("Analyzing...")
        file=request.files['file']
        logging.info(f"Uploaded: {file.filename}")
        logging.info(f"File size: {len(file.read())} bytes")
        try:
            content = Content(uploadFile(file)[1])
            content.summarize()
            content.getKeywords()
            content.getPolarity()

            newFile = File(fileName=file.filename, userId=current_user.id, fileSize=len(file.read()), fileSummary=content.summary)
            db.session.add(newFile)
            db.session.commit()

            logging.info(f"Summary: {content.summary}")
            logging.info(f"Keywords: {content.keywords}")
            logging.info(f"Poliarity: {content.polarity}")
            return render_template('document_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('document.html', user=current_user)

@views.route('/text', methods=['GET', 'POST'])
@login_required
def text():
    if request.method == 'POST':
        logging.info("Analyzing...")
        text=request.form.get('text')
        try:
            content = Content(text)
            content.summarize()
            content.getKeywords()
            content.getPolarity()

            logging.info(f"Summary: {content.summary}")
            logging.info(f"Keywords: {content.keywords}")
            logging.info(f"Polarity: {content.polarity}")
            return render_template('text_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('text.html', user=current_user)