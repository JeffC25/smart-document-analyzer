import json
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def analyze(fileID, userID):
    keywords = {'foo','bar'}

    