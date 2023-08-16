from login_system import login_user
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="jwad",
  password="jwad4512",
  database="bank_system_history"
)
mycursor = mydb.cursor()

