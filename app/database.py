# DEPRECATED -- DO NOT USE

import sqlite3

database = "database.db"

def createDatabase():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    usersTable = """CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY, 
        username TEXT UNIQUE, 
        path UNIQUE);"""
    cursor.execute(usersTable)

    filesTable = """CREATE TABLE IF NOT EXISTS files(
        file_id INTEGER PRIMARY KEY, 
        file_name TEXT,
        user_id INTEGER,
        file_path STRING,
        file_size INTEGER, 
        file_summary TEXT,
        timestamp TEXT,
        FOREIGN KEY(user_id) REFERENCES users(user_id),
        UNIQUE(user_id, file_name));"""
    cursor.execute(filesTable)

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

    return 0
    
def uploadFile(fileName, user_id, filePath, fileSize, fileSummary, currTime):
    returnCode = 0
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    command = """INSERT INTO files (file_name, user_id, file_path, file_size, file_summary, timestamp) 
        VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(command, (fileName, user_id, filePath, fileSize, fileSummary, currTime))

    connection.commit()
    connection.close()

    return returnCode

def renameFile(newName, user_id=None, file_id=None, file_name=None):
    returnCode = 0
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    try:
        if user_id and file_name:
            command = """UPDATE files
                SET file_name = (?) WHERE file_name = (?) AND user_id = (?)"""
            cursor.execute(command, (newName, file_name, user_id))
        elif file_id:
            command = """UPDATE files
                SET file_name = (?) WHERE file_id"""
            cursor.execute(command, (newName, file_id))
        else:
            print("Invalid input")
            returnCode = -1

    except Exception as e:
        print(e)
        returnCode = -1

    connection.commit()
    connection.close()
    return returnCode


def deleteFile(user_id=None, file_name=None, file_id=None):
    returnCode = 0
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    try:
        if user_id and file_name:
            command = """DELETE FROM files
                WHERE user_id = (?) AND file_name = (?)"""
            cursor.execute(command, (user_id, file_name))
        elif file_id:
            command = """DELETE FROM files
                WHERE file_id = (?) """
            cursor.execute(command, (file_id,))
        else:
            print("Invalid input")
            returnCode = -1

    except Exception as e:
        print(e)
        returnCode = -1

    connection.commit()
    connection.close()
    return returnCode


def getUserPath(user_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    res = cursor.execute("SELECT path FROM users WHERE user_id = ?", (user_id,))
    res.fetchone()

    connection.commit()
    connection.close()

    return 0, res[0]

def addKeyword(keyword): 
    returnCode = 0

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    command = """INSERT INTO keywords (keywrod) VALUES (?)"""
    cursor.execute(command, (keyword,))

    connection.commit()
    connection.close()

    return returnCode


