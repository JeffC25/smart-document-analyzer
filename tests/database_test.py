import sys
sys.path.append('../')
from main import database

# create database
database.createDatabase()

# upload files - uploadFile(fileName, user_id, filePath, fileSize, currTime)
print(database.uploadFile("fileName.txt", 1, "filePath", 64, "currTime") )
print(database.uploadFile("oldName.txt", 2, "anotherfilepath", 128, "currTime" ))
print(database.uploadFile("drop.txt", 3, "'", 432, "time); DROP TABLE users"))
print(database.uploadFile("filetodelete.txt", 4, "examplepath", 32, "time" ))
print(database.uploadFile("filetodelete2.txt", 4, "examplepath", 32, "time" ))

# deleting files - deleteFile(user_id, file_name)
# deleting files - deleteFile(user_id=None, file_name=None, file_id=None)
print(database.deleteFile(user_id=4, file_name="filetodelete.txt"))
# database.deleteFile(file_id=4)

# renameing files - renameFile(user_id, file_name, newName)
print(database.renameFile("2", "oldName.txt", "newName.txt"))