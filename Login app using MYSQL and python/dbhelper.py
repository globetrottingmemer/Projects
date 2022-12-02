import mysql.connector
import sys
class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost", user="root", password="", database="my-sql-demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Some Error occured")
            sys.exit(0)
        else:
            print("Connected to database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO users (id,name,email,password) 
            VALUES (NULL, '{}','{}','{}')""".format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            1

    def search(self,email,password):

        self.mycursor.execute("""
                    SELECT * From users WHERE email LIKE '{}' AND password LIKE '{}'
                    """.format(email, password))

        data = self.mycursor.fetchall()
        self.conn.commit()
        return data


