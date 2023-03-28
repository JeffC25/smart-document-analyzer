import PyPDF2
import sqlite3
import io
import os
import asyncio
from flask import Flask, render_template, request, redirect, url_for
import database.database
import datetime

app = Flask(__name__)

async def uploadFile(file, userID, fileName=None):
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

    row = cursor.execute("SELECT path FROM customers WHERE user_id = ?", (userID,))
    row.fetchone()
    filePath = row[0]

    database.uploadFile(fileName, userID, filePath, fileSize, formattedTime)

    connection.commit()
    connection.close()

@app.route('/upload', methods=['POST'])
async def asyncUpload():
    file = request.files['file']
    task = asyncio.create_task(uploadFile(file))
    return await task

    # if path == "valid" and type == "valid":
    #     return {"data": "file uploaded successfully"}
    # return {"data": "upload unsuccessful"}