import mysql.connector


conn = mysql.connector.connect(host = "localhost", user="root", password="", database="my-sql-demo")
mycursor = conn.cursor()




