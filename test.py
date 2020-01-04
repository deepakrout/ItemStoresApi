import sqlite3

connection = sqlite3.connect('sec4-data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

users = [
    (1, 'deep', 'test'),
    (2, 'jose', 'test'),
    (3, 'rolf', 'test'),
]

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.executemany(insert_query,users)

connection.commit()
connection.close()