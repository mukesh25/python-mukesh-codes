import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="telusko")
mycursor = mydb.cursor()
mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in result:
	print(i)