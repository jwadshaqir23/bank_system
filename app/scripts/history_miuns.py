from login_system import login_user
pos = "_history_miuns"
GREEN = "\033[91m"
RESET = "\033[0m"
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="history_bank"
)
mycursor = mydb.cursor()

def print_colored_text(color, text):
    print(f"{color}{text}{RESET}")

def print_first_row():
    mycursor.execute(f"SELECT how_much FROM {login_user+pos} LIMIT 1")
    myresult = mycursor.fetchall()

    for x_mon in myresult:
        monney = str(x_mon[0])
        #print(monney)

    mycursor.execute(f"SELECT reason FROM {login_user+pos} LIMIT 1")
    myresult = mycursor.fetchall()

    for x_re in myresult:
        reason = str(x_re[0])
        #print(reason)

    mycursor.execute(f"SELECT who_pos_to FROM {login_user+pos} LIMIT 1")
    myresult = mycursor.fetchall()

    for x_pos_to in myresult:
        pos_to_who = str(x_pos_to[0])
        #print(who)

    mycursor.execute(f"SELECT date FROM {login_user+pos} LIMIT 1")
    myresult = mycursor.fetchall()

    for x_date in myresult:
        date = str(x_date[0])

    #print("$"+monney+"\nfrom:"+who+"\nreason:"+reason+"\ndate:"+date+"\n########################################")
    print_colored_text(GREEN,"$"+monney+"\nto:"+pos_to_who+"\nreason:"+reason+"\ndate:"+date)
    print("########################################")
def print_other_rows():
    offset = 1
    while True:
        mycursor.execute(f"SELECT how_much FROM {login_user+pos} LIMIT 1 OFFSET {offset}")
        myresult = mycursor.fetchall()

        if not myresult:  
            break

        for x_monney in myresult:
            monney = str(x_monney[0])
            #print(monney)

        mycursor.execute(f"SELECT reason FROM {login_user+pos} LIMIT 1 OFFSET {offset}")
        myresult = mycursor.fetchall()

        if not myresult:  
            break

        for x_re in myresult:
            reason = str(x_re[0])
            #print(reason)
        
        mycursor.execute(f"SELECT who_pos_to FROM {login_user+pos} LIMIT 1 OFFSET {offset}")
        myresult = mycursor.fetchall()

        if not myresult:  
            break

        for x_pos_to in myresult:
            pos_to_who = str(x_pos_to[0])
            #print(who)

        mycursor.execute(f"SELECT date FROM {login_user+pos} LIMIT 1 OFFSET {offset}")
        myresult = mycursor.fetchall()

        if not myresult:  
            break

        for x_date in myresult:
            date = str(x_date[0])
            #print(who)

        
        #print("$"+monney+"\nfrom:"+who+"\nreason:"+reason+"\ndate:"+date+"\n########################################")
        print_colored_text(GREEN,"$"+monney+"\nto:"+pos_to_who+"\nreason:"+reason+"\ndate:"+date+"")
        print("########################################")
        offset += 1  


print_first_row()
print_other_rows()

