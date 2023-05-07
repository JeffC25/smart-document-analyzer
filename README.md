# Smart Document Analyzer Overview

This project is a document analyzer implemented in Flask and allows users to generate summaries, keywords, and sentiment from PDF files, news article URLs, or manual text input. It consists of the following major component: a database, PDF uploader, news article ingester, NLP sentiment module, and a frontend UI created with Bootstrap. The project is packaged using Docker.

## Database Overview 

The database was implemented with SQLAlchemy and SQLite3. It currently consists of 4 tables: a User table , File table, Keyword table, and Keyword Pairing table

Each row of the User table stores information regarding each user's ID, username, email, and (hashed) password

Each row of the File table stores information regarding each file's ID, name, owner ID (foreign key), size, summary, and time of upload

Each row of the Keyword table stores keywords and ID

Each row of the Keyword Pairing table stores a file ID (foreign key) and keyword ID (foreign key)

## PDF Uploader

The PDF uploader module uses the PyPdf library to read a PDF file and output its text contents.

## News Article Ingester

The news article ingester module uses the newspaper3k to load an article specified by its URL. The module is responsible for parsing the article and outputting its text contents.

## NLP Sentiment

The NLP sentiment module implements a Content() class that takes in a text. It consists of methods that generate for the text a summary, list of keywords, and sentiment.

It uses a simple extractive text algorithm that generates its analysis by utilizing stopwords, word frequencies, and sentence weights in conjunction with the NLTK, TextBlob, and Yake libraries.

## Instructions:

1. Run `git clone git@github.com:ECE530-2023/news-analyzer-JeffC25.git` to clone the repository
2. Create a `.env` file in the cloned directory and populate it with `SECRET_KEY=<your secret key>`
3. Run `pip install -r requirements.txt` to install Python dependencies
4. Run `apt-get install sqlite3` to install SQLite3
5. Run `python3 main.py` to launch the Flask application
