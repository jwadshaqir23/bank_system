import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="jwad",
  password="jwad4512",
  database="bank_system"
)
mycursor = mydb.cursor()

user_login_loop = True
while user_login_loop:
  login_user = input("username: ")
  mycursor.execute(f"SELECT username FROM login_system where username = '{login_user}' LIMIT 1")
  if mycursor.fetchall():
    os.system("cls")
    user_login_loop = False
    pass_login_loop = True
  else:
    os.system("cls")
    print("username is in,correct,try agin")  

# while pass_login_loop:
#   login_pass = input("password: ")
#   mycursor.execute(f"SELECT password FROM login_system where password = '{login_pass}' LIMIT 1")
#   if mycursor.fetchall():
#     os.system("cls")
#     pass_login_loop = False
#     login_system_loop_passing = True
    
#   else:
#     os.system("cls")
#     print("password isn,t correct,try agin")

while pass_login_loop:
   #
  login_pass = input("password: ")
  mycursor.execute(f"SELECT password FROM login_system WHERE username = '{login_user}'")
  myresult = mycursor.fetchall()
  for x_pass_check in myresult:
              
              sys_pass_check = str(x_pass_check[0])
  if sys_pass_check == login_pass:
    pass_login_loop = False
    login_system_loop_passing = True
  else:
     print("password isn`t correct ,try agin please")