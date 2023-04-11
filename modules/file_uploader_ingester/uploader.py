import PyPDF2
import sqlite3
import io
import os
import datetime
import json
from flask import Flask, render_template, request, redirect, url_for
import importlib

import sys
sys.path.append('./database')
import database

app = Flask(__name__)

def uploadFile(file, userID, fileName=None):
    reader = PyPDF2.PdfFileReader(io.BytesIO(file.read()))
    numPages = reader.getNumPages()
    fileData = file.read()

    if fileName == None:
        fileName = file.filename()

    fileSize = os.fstat(file).st_size

    currentTime = datetime.datetime.now()
    formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")

    textContent = ''
    for page in reader.pages:
        textContent += page.extract_text()

    filePath = database.getUserPath(userID)
    database.uploadFile(fileName, userID, filePath, fileSize, formattedTime)

    return {"data": "file uploaded successfully"}
    # return {"data": "upload unsuccessful"}