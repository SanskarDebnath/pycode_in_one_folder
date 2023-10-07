import mysql.connector

#pip install mysql-connector-python

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0381",
    db = "mysql_python"
)
new_object = database.cursor()

# new_record = """
# CREATE TABLE RECORDS (NAME VARCHAR (40), STUDENT_ID INT PRIMARY KEY, UNIV_NUM INT UNIQUE, ADDRESS VARCHAR (40))
# """

# new_object.execute(new_record)

# data_record = """
# INSERT INTO RECORDS VALUES ('SANSKAR DEBNATH', 213040, 5555, 'MADHAV')
# """
# new_object.execute(data_record)

sql = "select * from records"
new_object.execute(sql)

