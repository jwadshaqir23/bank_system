import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system"
)
mycursor = mydb.cursor()

# from login_system import login_user
# from first_app import welcome_print
# print("welcome "+welcome_print)


from login_system import login_user

os.system("cls")

choose_loop = True
while choose_loop:
    #
  print("1;view balance")
  print("2;send money")
  print("3;request money")
  print("4;view history")

  choose = input(">>>")

  if choose == "1":
      import scripts.view_balance
      input("hit any key to continue")
      os.system("cls")
  elif choose == "2":
      import scripts.send_money_system
      input("hit any key to continue")
      os.system("cls")
  elif choose == "3":
      import scripts.request_money_system
      input("hit any key to continue")
      os.system("cls")
  elif choose == "4":
      os.system("cls")
      import scripts.view_history
      input("hit any key to continue")
  else:
      print("undefined input ,try agin")
      input("hit any key to continue")
      os.system("cls")