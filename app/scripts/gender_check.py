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
mycursor.execute(f"SELECT gender FROM login_system WHERE username Like '{login_user}'")
myresult = mycursor.fetchall()
for x_user_gen in myresult:
 
 user_gender = str(x_user_gen[0])
  
if user_gender == "men":
 is_the_user_men = True
 is_the_user_women = False
elif user_gender == "women":
 is_the_user_women = True
 is_the_user_men = False