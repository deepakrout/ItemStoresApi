import sqlite3

connection = sqlite3.connect('sec6-data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
connection.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items ( id INTEGER PRIMARY KEY, name text, price real)"
connection.execute(create_table)


connection.commit()
connection.close()