import mysql.connector

#pip install mysql-connector-python

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0381"
)
# print (database)


# # preparing a cursor object
# sanskar = database.cursor()
 
# # creating database
# sanskar.execute("CREATE DATABASE mysql_python")

# #sanskar.execute("SHOW DATABASES")

print("s")