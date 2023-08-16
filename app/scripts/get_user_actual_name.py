import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system"
)
mycursor = mydb.cursor()
from login_system import login_user

mycursor.execute(f"SELECT actual_name FROM login_system WHERE username Like '{login_user}'")
myresult = mycursor.fetchall()
for x_user_actual_name in myresult:
 
 user_actual_name = str(x_user_actual_name[0])