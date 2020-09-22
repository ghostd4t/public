#coding: UTF-8
import mysql.connector
import convertver

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='#####',
        passwd='#########',
        database='########'
    )
except:
    print('can\'t connect to the server')

mycursor = mydb.cursor()
sqlFormula = "INSERT INTO testing2 (class, class_letter, name, surname) VALUES (%s, %s, %s, %s)"
for data in bigdata:
    mycursor.execute(sqlFormula, data)
mydb.commit()

"""
use school_app;

CREATE TABLE students_list
(
class int primary key, 
class_letter varchar(10),
name varchar(30),
surname varchar(30)
);
"""