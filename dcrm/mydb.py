#Install Mysql on your computer
# https://div.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector
dataBase= mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "9LxQUmHC$m5i!8"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")