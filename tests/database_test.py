import sys
sys.path.append('../')
from app import database

# # create database
# database.createDatabase()

# # upload files - uploadFile(fileName, user_id, filePath, fileSize, fileSummary, currTime)
# print(database.uploadFile("fileName.txt", 1, 64, "summary", "currTime") )
# print(database.uploadFile("oldName.txt", 2, 128, "summary", "currTime" ))
# print(database.uploadFile("time); DROP TABLE users", 3, "'", 432, "time); DROP TABLE users", "today"))
# print(database.uploadFile("filetodelete.txt", 4, 32, "summary", "time" ))
# print(database.uploadFile("filetodelete2.txt", 4, 32, "summary", "time" ))

# # deleting files - deleteFile(user_id, file_name)
# # deleting files - deleteFile(user_id=None, file_name=None, file_id=None)
# print(database.deleteFile(user_id=4, file_name="filetodelete.txt"))
# # database.deleteFile(file_id=4)

# # renameing files - renameFile(user_id, file_name, newName)
# print(database.renameFile("2", "oldName.txt", "newName.txt"))