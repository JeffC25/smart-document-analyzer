from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import File, User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .nlp import Content
from .nfi import getArticle
from .sfu import uploadFile

# define routes
views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
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

            # return redirect(url_for('views.article_analysis'))
            return render_template('article_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('article.html', user=current_user)


@views.route('/document', methods=['GET', 'POST'])
@login_required
def document():
    if request.method == 'POST':
        print("Analyzing...")
        file=request.files['file']
        print(f"Uploaded: {file.filename}")
        print(f"File size: {len(file.read())} bytes")
        try:
            # document = file.read()
            content = Content(uploadFile(file)[1])
            content.summarize()
            content.getKeywords()
            content.getPolarity()

            newFile = File(fileName=file.filename, userId=current_user.id, fileSize=len(file.read()), fileSummary=content.summary)
            db.session.add(newFile)
            db.session.commit()

            return render_template('document_results.html', user=current_user, summary=content.summary, keywords=content.keywords, polarity=content.polarity)
        
        except Exception as e:
            flash(f'Error: {e}', category='error')
    
    return render_template('document.html', user=current_user)