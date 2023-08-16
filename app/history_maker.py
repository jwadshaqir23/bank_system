from login_system import login_user
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system_history"
)
mycursor = mydb.cursor()

