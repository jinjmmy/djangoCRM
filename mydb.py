import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jin@7132'
)

#prep cursor
cursorObj = dataBase.cursor()

#create db

cursorObj.execute('CREATE DATABASE neura')
print("all done")