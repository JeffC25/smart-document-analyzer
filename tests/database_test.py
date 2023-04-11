import sys
sys.path.append('../modules')
from database import database
import file_uploader_ingester.uploader
import sqlite3

database.createDatabase()

database.uploadFile("fileName.txt", 1, "filePath", 64, "currTime")  # Simple test
database.uploadFile("drop.txt", 2, "'", 432, "time); DROP TABLE users") # Injection test