import PyPDF2
import sqlite3
import io
import os
from flask import Flask, render_template, request, redirect, url_for
import database.database
import datetime

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

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    row = cursor.execute("SELECT path FROM users WHERE user_id = ?", (userID,))
    row.fetchone()
    filePath = row[0]

    database.uploadFile(fileName, userID, filePath, fileSize, formattedTime)

    connection.commit()
    connection.close()

    return {"data": "file uploaded successfully"}
    # return {"data": "upload unsuccessful"}