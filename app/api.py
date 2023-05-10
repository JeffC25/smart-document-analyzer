from flask import Blueprint, render_template, request, flash, jsonify, abort
from flask_login import login_user, login_required, logout_user, current_user
from .nlp import Content
from .nfi import getArticle
from .sfu import uploadFile
from .models import File, User
from . import db
import logging

# define routes
api = Blueprint('api', __name__)

@api.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@api.route('/article=<path:article>', methods=['GET', 'POST'])
@login_required
def article(article):
    try:
        content = Content(getArticle(article)[1])
        content.summarize()
        content.getKeywords()
        content.getPolarity()

        logging.info(f"Summary: {content.summary}")
        logging.info(f"Keywords: {content.keywords}")
        logging.info(f"Polarity: {content.polarity}")

        return jsonify({"polarity": content.polarity,
                        "summary": content.summary,
                        "keywords": list(content.keywords)
                        })
    
    except Exception as e:
        logging.warn(e)
        pass
    
    return jsonify()


@api.route('/text=<path:text>', methods=['GET', 'POST'])
@login_required
def text(text):
    try:
        content = Content(text)
        content.summarize()
        content.getKeywords()
        content.getPolarity()

        logging.info(f"Summary: {content.summary}")
        logging.info(f"Keywords: {content.keywords}")
        logging.info(f"Polarity: {content.polarity}")

        return jsonify({"polarity": content.polarity,
                        "summary": content.summary,
                        "keywords": list(content.keywords)
                        })
    
    except Exception as e:
        logging.warn(e)
        pass

    return jsonify()