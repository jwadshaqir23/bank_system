import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="jwad",
  password="jwad4512",
  database="bank_system"
)
mycursor = mydb.cursor()
from login_system import login_user
from login_system import login_user
mycursor.execute(f"SELECT email FROM login_system WHERE username Like '{login_user}'")
myresult = mycursor.fetchall()
for x_user_email in myresult:
 
 user_email = str(x_user_email[0])