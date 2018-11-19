# MySQL tutorials
# https://www.w3schools.com/python/python_mysql_getstarted.asp
# https://www.youtube.com/watch?v=bEtnYWuo2Bw

# Create Table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
#mycursor.execute("SHOW TABLES")

# Primary Key

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mydatabase"
)
mycursor = mydb.cursor()

#sql = "INSERT INTO students (name, address) VALUES (%s, %s)"
#val = ('Ben', 'Park Lane 38')

mycursor.execute("SELECT name, address FROM students")

#mydb.commit()

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
#print("1 record inserted, ID:", mycursor.lastrowid)


