import mysql.connector
def background_function(mydb,mycursor):
    while True:
        mydb = mysql.connector.connect(
        host="localhost",
        user="bank_agent",
        password="bank_agent",
        database="bank_system"
        )
        mycursor = mydb.cursor()

background_function(mydb,mycursor)