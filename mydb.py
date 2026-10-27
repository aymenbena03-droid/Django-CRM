# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root', 
    password = 'aymen10',
)

# prepare a cursor object 
cursorObject = dataBase.cursor()

# create a datebase 
cursorObject.execute("CREATE DATABASE test")

print("All Done!")
