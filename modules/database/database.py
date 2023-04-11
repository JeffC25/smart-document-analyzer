import sqlite3

database = 'database.db'

def createDatabase():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    usersTable = """CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY, 
        username TEXT UNIQUE, 
        full_name TEXT, 
        path UNIQUE);"""
    cursor.execute(usersTable)

    filesTable = """CREATE TABLE IF NOT EXISTS files(
        file_id INTEGER PRIMARY KEY, 
        file_name TEXT,
        user_id INTEGER,
        file_path STRING,
        file_size INTEGER, 
        timestamp TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id));"""
    cursor.execute(filesTable)

    paragraphsTable = """CREATE TABLE IF NOT EXISTS paragraphs(
        paragraph_id INTEGER PRIMARY KEY,
        file_id INTEGER, 
        sentiment INTEGER,
        FOREIGN KEY(file_id) REFERENCES files(file_id));"""
    cursor.execute(paragraphsTable)

    keywordsTable = """CREATE TABLE IF NOT EXISTS keywords(
        keyword_id INTEGER PRIMARY KEY, 
        keyword TEXT);"""
    cursor.execute(keywordsTable)

    kppairTable = """CREATE TABLE IF NOT EXISTS kppair(
        keyword_id INTEGER,
        file_id INTEGER,
        FOREIGN KEY(keyword_id) REFERENCES keywords(keyword_id),
        FOREIGN KEY(file_id) REFERENCES files(file_id))"""
    cursor.execute(kppairTable)

    connection.commit()
    connection.close()
    

def uploadFile(fileName, user_id, filePath, fileSize, currTime):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    command = "INSERT INTO files (file_name, user_id, file_path, file_size, timestamp) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(command, (fileName, user_id, filePath, fileSize, currTime))

    connection.commit()
    connection.close()

def renameFile(user_id, fileName, newName):
    return

def deleteFile(user_id, fileName):
    return

def getUserPath(user_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    res = cursor.execute("SELECT path FROM users WHERE user_id = ?", (user_id,))
    res.fetchone()

    connection.commit()
    connection.close()

    return res[0]