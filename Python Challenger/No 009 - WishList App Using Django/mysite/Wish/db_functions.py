# IMPORT [SQLITE]
import sqlite3 as lite

con = lite.connect('wish-database.db')
cur = con.cursor()

def createWish():
    pass

def readWish():
    command = "SELECT * FROM wish_list"
    cur.execute(command)
    values = cur.fetchall()

    return values

def updateWish():
    pass

def deleteWish():
    pass
