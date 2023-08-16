import mysql.connector
import os
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="jwad",
  password="jwad4512",
  database="bank_system"
)
mycursor = mydb.cursor()
from login_system import login_user

def generate_random_code(digits):
    code = ''.join(str(random.randint(0, 9)) for _ in range(digits))
    return code

random_code = generate_random_code(8)

def random_code_check_db(fun_code):
    mycursor.execute(f"SELECT req_code FROM req_mon_cod where req_code = '{fun_code}' LIMIT 1")
    if mycursor.fetchall():
        fun_code = generate_random_code(8)
    else:
        return fun_code
    
    
random_code_check_db(random_code)
def request_money():
    #
    sql ="INSERT INTO req_mon_cod(username,req_code,cod_open_date) VALUES(%s,%s,%s)"
    data = (login_user,random_code,"none for later")
    mycursor.execute(sql,data)
    mydb.commit()
    print("here is your money request code: "+random_code)



sure_loop = True
while sure_loop:
    #
    print("are you sure to to get a money request code?")
    sure = input("[yes/no]:")

    if sure == "yes":
        request_money()
        sure_loop = False
    elif sure == "no":
        sure_loop = False
    else:
        print("wrong input try agin please")