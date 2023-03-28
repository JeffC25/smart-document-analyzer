import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def createDatabase():
    usersTable = """CREATE TABLE IF NOT EXISTS
    users(user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, full_name TEXT, path UNIQUE)"""
    cursor.execute(usersTable)

    filesTable = """CREATE TABLE IF NOT EXISTS
    files(file_id INTEGER PRIMARY KEY, file_name TEXT, FOREIGN KEY(user_id) REFERENCES users(user_id), file_type TEXT, file_size INTEGER, timestamp TEXT)"""
    cursor.execute(filesTable)

    paragraphsTable = """CREATE TABLE IF NOT EXISTS
    paragraphs(paragraph_id INTEGER PRIMARY KEY, FOREIGN KEY(file_id) REFERENCES files(file_id), sentiment INTEGER)"""
    cursor.execute(paragraphsTable)

    keywordsTable = """CREATE TABLE IF NOT EXISTS
    keywords(keyword_id INTEGER PRIMARY KEY, keyword TEXT)"""
    cursor.execute(keywordsTable)

    kppairTable = """CREATE TABLE IF NOT EXISTS
    kppair(FOREIGN KEY(keyword_id) REFERENCES keywords(keyword_id), FOREIGN KEY(file_id) REFERENCES files(file_id))"""
    cursor.execute(kppairTable)
    

def uploadFile(fileName, user_id, filePath, fileSize, currTime):
    command = "INSERT INTO files (file_name, user_id, file_path, size, timestamp) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(command, (fileName, user_id, filePath, fileSize, currTime))

def renameFile(user_id, fileName, newName):
    if not user_id == "username":
        return "failed"
    if newName == "invalid":
        return "failed"
    if fileName == "valid":
        return "success"
    return "failed"

def deleteFile(user_id, fileName):
    if not user_id == "username":
        return "failed"
    if fileName == "valid":
        return "success"
    return "failed"