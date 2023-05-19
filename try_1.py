import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
 password= None,
 database="facebook"
)
print(mydb)