import sys
sys.path.append('../modules')
from database import database
from file_uploader_ingester import uploader
import sqlite3

# create database
database.createDatabase()

# upload files - uploadFile(fileName, user_id, filePath, fileSize, currTime)
database.uploadFile("fileName.txt", 1, "filePath", 64, "currTime") 
database.uploadFile("oldName.txt", 2, "anotherfilepath", 128, "currTime" )
database.uploadFile("drop.txt", 3, "'", 432, "time); DROP TABLE users")
database.uploadFile("filetodelete.txt", 4, "examplepath", 32, "time" )

# deleteing files - deleteFile(user_id, file_name)
database.deleteFile("4", "filetodelete.txt")

# renameing files - renameFile(user_id, file_name, newName)
database.renameFile("2", "oldName.txt", "newName.txt")