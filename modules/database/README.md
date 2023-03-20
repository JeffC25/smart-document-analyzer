# Database Design

The data base will use a SQL schema with tables for users, files, paragraphs, and keywords

# Users

user_id (primary key)

username

full_name

path

# Files

file_id (primary key)

file_name

user_id (foreign key)

timestamp

file_type

file_path

size

# Paragraphs

paragraph_id (primary key)

file_id (foreign key)

sentiment

# keywords

paragraph_id

keywords
