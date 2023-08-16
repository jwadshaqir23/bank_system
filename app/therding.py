import mysql.connector
def background_function(mydb,mycursor):
    while True:
        mydb = mysql.connector.connect(
        host="localhost",
        user="jwad",
        password="jwad4512",
        database="bank_system"
        )
        mycursor = mydb.cursor()

background_function(mydb,mycursor)