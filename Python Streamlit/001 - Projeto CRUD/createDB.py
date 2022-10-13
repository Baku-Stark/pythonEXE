import sqlite3 as lite

con = lite.connect('database/database.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE client_users(id INTEGER PRIMARY KEY AUTOINCREMENT, users_name TEXT, users_age TEXT, users_profession TEXT)")