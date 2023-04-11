import sys
sys.path.append('../modules')
from database import database
import file_uploader_ingester.uploader
import sqlite3

database.createDatabase()
database.uploadFile("fileName.txt", 1, "filePath", 64, "currTime")

#     createDatabase()
#     uploadFile("ex.txt", 404, "path", "pdf", 404,"time")