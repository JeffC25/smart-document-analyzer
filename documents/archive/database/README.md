# Database Design

The data base will use a SQL schema with tables for users, files, paragraphs, and keywords

# Users Table

user_id (primary key)

username

full_name

path

# Files Table

file_id (primary key)

file_name

user_id (foreign key)

file_path

size

timestamp

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