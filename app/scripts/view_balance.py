def start_view_balance():
  import mysql.connector
  import os
  mydb = mysql.connector.connect(
    host="localhost",
    user="bank_agent",
    password="bank_agent",
    database="bank_system"
  )
  mycursor = mydb.cursor()
  os.system("cls")
  from login_system import login_user

  mycursor.execute(f"SELECT balance FROM bank_accounts_info WHERE username Like '{login_user}'")
  myresult = mycursor.fetchall()
  for x_user_balance in myresult:

      user_balance = str(x_user_balance[0])
  print("your balance:"+"$"+user_balance)