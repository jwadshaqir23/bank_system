from login_system import login_user
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system"
)
mycursor = mydb.cursor()


to_who_loop = True
while to_who_loop:
    os.system("cls")

    print("to who(account name")
    to_who = input(">>>")

        
    mycursor.execute(f"SELECT username FROM bank_accounts_info where username = '{to_who}' LIMIT 1")
    if mycursor.fetchall():
        to_who_loop = False
        how_much_loop = True
    else:
        print("there is something wrong with the account name ,please try agin...")

while how_much_loop:
    print("how much do you want to transfer ?")
    how_much = input(">>>")

    mycursor.execute(f"SELECT balance FROM bank_accounts_info where balance <= '{how_much}' LIMIT 1")
    if mycursor.fetchall():
        print("very good")
    else:
        print("there is something wrong with the account name ,please try agin...")
