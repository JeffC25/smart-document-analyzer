# Database Design

The data base will use a SQL schema with tables for users, files, paragraphs, and keywords

# Users Table

user_id (primary key)

username

full_name

path

# Files

file_id (primary key)

file_name

user_id (foreign key)

file_type

file_path

size

def uploadFile(user_id, fileName, fileType, fileSize):
    currentTime = datetime.datetime.now()
    formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    command = f"INSERT INTO files (file_id, file_name, user_id, timestamp, file_type, file_path, size) VALUES ({fileName}, {user_id}, {formattedTime}, {fileType}, {fileSize})"
    cursor.execute(command)

# Paragraphs Table

paragraph_id (primary key)

file_id (foreign key)

sentiment

# Keywords Table

keyword_id (primary key)

keyword

# Keyword-Paragraph Junction Table

keyword_id (secondary key)

file_id (secondary key)

