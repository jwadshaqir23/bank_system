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



print("welcome to send money panel")
hoole_tran_loop = True
while hoole_tran_loop:
    #
    send_code = input("your request code please: ")

    mycursor.execute(f"SELECT req_code FROM req_mon_cod where req_code = '{send_code}' LIMIT 1")
    if mycursor.fetchall():
        mycursor.execute(f"SELECT username FROM req_mon_cod WHERE req_code Like '{send_code}'")
        myresult = mycursor.fetchall()
        for x_name_check in myresult:
            #
            sys_name_check = str(x_name_check[0])
        if sys_name_check == login_user:
            print("you can`t send money to your self")
        else:

            print("how much money do you need to send to "+sys_name_check)
            tran_how_much = input(">>>")
            mycursor.execute(f"SELECT balance FROM bank_accounts_info where username = '{login_user}' LIMIT 1")
            myresult = mycursor.fetchall()
            for x_user_balan in myresult:
            #
                sys_user_balan = str(x_user_balan[0])
            if tran_how_much > sys_user_balan:
                print("with this much of money your money balance will be in the miuns")
                print("are you sure to confirm that transaction?")
                making_sure_of_tran = input("[yes/no]: ")
                if making_sure_of_tran == "yes":
                    reason_of_tran = input("reason of transaction: ")
                    int_user_balance = int(sys_user_balan)
                    int_tran_how_much = int(tran_how_much)
                    calculate_after_tran_bala =  int_user_balance - int_tran_how_much
                    print("after this transaction your account balance will be "+str(calculate_after_tran_bala))
                    print("Recipient account name: "+sys_name_check)
                    mycursor.execute(f"SELECT actual_name FROM login_system WHERE username Like '{sys_name_check}'")
                    myresult = mycursor.fetchall()
                    for x_rec_actual_name in myresult:
                    
                        rec_actual_name = str(x_rec_actual_name[0])
                    print("Recipient real name: "+rec_actual_name)
                    print("transaction code:"+send_code)
                    print("-----------------------------------------------------")
                    print("are sure about this transaction?")
                    making_sure_of_tran_final = input("[yes/no]")
                    if making_sure_of_tran_final == "yes":
                        verfiy_code_loop = True
                        while verfiy_code_loop:
                            #
                            print("we sent a verfication code to your email ")
                            print("please type it here")
                            import scripts.verfying_system.email_verfiy
                            from scripts.verfying_system.email_verfiy import verfiy_code_number
                            verfiy_code = input("your verfiy code that in your email:")
                            if verfiy_code == verfiy_code_number:
                                    #get recepient actual balance and calulate it to the new balance
                                    mycursor.execute(f"SELECT balance FROM bank_accounts_info where username = '{sys_name_check}' LIMIT 1")
                                    myresult = mycursor.fetchall()
                                    for x_rece_balan in myresult:
                                        sys_rece_balan = str(x_rece_balan[0])
                                    int_sys_rece_balan = int(sys_rece_balan)
                                    rece_how_much_after_tran = int_sys_rece_balan + int_tran_how_much
                                    ##########
                                    #adding money
                                    sql ="UPDATE bank_accounts_info SET balance = %s WHERE username = %s"
                                    data = (rece_how_much_after_tran,sys_name_check)
                                    mycursor.execute(sql,data)
                                    mydb.commit()
                                    #deleting money
                                    sql ="UPDATE bank_accounts_info SET balance = %s WHERE username = %s"
                                    data = (calculate_after_tran_bala,login_user)
                                    mycursor.execute(sql,data)
                                    mydb.commit()
                                    #adding history for transacter
                                    tran = "_history_tran"
                                    database2_name = 'history_bank'
                                    database1_name = 'bank_system'
                                    mycursor.execute(f"USE {database2_name}")
                                    sql =f"INSERT INTO {login_user+tran}(recivier,how_much,acc_num,reason) VALUES(%s,%s,%s,%s)"
                                    data = (rec_actual_name,tran_how_much,sys_name_check,reason_of_tran)
                                    mycursor.execute(sql,data)
                                    mydb.commit()
                                    #adding history for recpe
                                    mycursor.execute(f"USE {database1_name}")
                                    mycursor.execute(f"SELECT actual_name FROM login_system WHERE username Like '{login_user}'")
                                    myresult = mycursor.fetchall()
                                    for x_user_actual_name in myresult:
                                        user_actual_name = str(x_user_actual_name[0])
                                    import datetime
                                    current_date = datetime.datetime.now()
                                    formatted_date = current_date.strftime("%d-%m-%Y")
                                    pos = "_history_pos"
                                    mycursor.execute(f"USE {database2_name}")
                                    sql =f"INSERT INTO {sys_name_check+pos}(how_much,reason,from_who,date) VALUES(%s,%s,%s,%s)"
                                    data = (tran_how_much,reason_of_tran,user_actual_name,formatted_date)
                                    mycursor.execute(sql,data)
                                    mydb.commit()
                                    #deleting transaction code
                                    mycursor.execute(f"USE {database1_name}")
                                    sql_query = "DELETE FROM req_mon_cod WHERE req_code = %s"
                                    mycursor.execute(sql_query, (send_code,))
                                    mydb.commit()
                                    print("tranaction sucssesfully good!")
                                    verfiy_code_loop = False
                                    hoole_tran_loop = False
                            else:
                                print("verfiy code is not correct")
                                print("please try agin")
                    if making_sure_of_tran_final == "no":
                        print("ok ,see you later ")
                if making_sure_of_tran == "no":
                    print("ok ,see you later")
            if tran_how_much < sys_user_balan:
                reason_of_tran = input("reason of transaction: ")
                int_user_balance = int(sys_user_balan)
                int_tran_how_much = int(tran_how_much)
                calculate_after_tran_bala =  int_user_balance - int_tran_how_much
                print("after this transaction your account balance will be "+str(calculate_after_tran_bala))
                print("Recipient account name: "+sys_name_check)
                mycursor.execute(f"SELECT actual_name FROM login_system WHERE username Like '{sys_name_check}'")
                myresult = mycursor.fetchall()
                for x_rec_actual_name in myresult:
                    
                    rec_actual_name = str(x_rec_actual_name[0])
                print("Recipient real name: "+rec_actual_name)
                print("transaction code:"+send_code)
                print("-----------------------------------------------------")
                print("are sure about this transaction?")
                making_sure_of_tran_final = input("[yes/no]")
                if making_sure_of_tran_final == "yes":
                    verfiy_code_loop = True
                    while verfiy_code_loop:
                        #
                        print("we sent a verfication code to your email ")
                        print("please type it here")
                        import scripts.verfying_system.email_verfiy
                        from scripts.verfying_system.email_verfiy import verfiy_code_number
                        verfiy_code = input("your verfiy code that in your email:")
                        if verfiy_code == verfiy_code_number:
                                #get recepient actual balance and calulate it to the new balance
                                mycursor.execute(f"SELECT balance FROM bank_accounts_info where username = '{sys_name_check}' LIMIT 1")
                                myresult = mycursor.fetchall()
                                for x_rece_balan in myresult:
                                    sys_rece_balan = str(x_rece_balan[0])
                                int_sys_rece_balan = int(sys_rece_balan)
                                rece_how_much_after_tran = int_sys_rece_balan + int_tran_how_much
                                ##########
                                #adding money
                                sql ="UPDATE bank_accounts_info SET balance = %s WHERE username = %s"
                                data = (rece_how_much_after_tran,sys_name_check)
                                mycursor.execute(sql,data)
                                mydb.commit()
                                #deleting money
                                sql ="UPDATE bank_accounts_info SET balance = %s WHERE username = %s"
                                data = (calculate_after_tran_bala,login_user)
                                mycursor.execute(sql,data)
                                mydb.commit()
                                #adding history for transacter
                                tran = "_history_tran"
                                database2_name = 'history_bank'
                                database1_name = 'bank_system'
                                mycursor.execute(f"USE {database2_name}")
                                sql =f"INSERT INTO {login_user+tran}(recivier,how_much,acc_num,reason) VALUES(%s,%s,%s,%s)"
                                data = (rec_actual_name,tran_how_much,sys_name_check,reason_of_tran)
                                mycursor.execute(sql,data)
                                mydb.commit()
                                #adding history for recpe
                                mycursor.execute(f"USE {database1_name}")
                                mycursor.execute(f"SELECT actual_name FROM login_system WHERE username Like '{login_user}'")
                                myresult = mycursor.fetchall()
                                for x_user_actual_name in myresult:
                                    user_actual_name = str(x_user_actual_name[0])
                                import datetime
                                current_date = datetime.datetime.now()
                                formatted_date = current_date.strftime("%d-%m-%Y")
                                pos = "_history_pos"
                                mycursor.execute(f"USE {database2_name}")
                                sql =f"INSERT INTO {sys_name_check+pos}(how_much,reason,from_who,date) VALUES(%s,%s,%s,%s)"
                                data = (tran_how_much,reason_of_tran,user_actual_name,formatted_date)
                                mycursor.execute(sql,data)
                                mydb.commit()
                                #deleting transaction code
                                mycursor.execute(f"USE {database1_name}")
                                sql_query = "DELETE FROM req_mon_cod WHERE req_code = %s"
                                mycursor.execute(sql_query, (send_code,))
                                mydb.commit()
                                print("tranaction sucssesfully good!")
                                verfiy_code_loop = False
                                hoole_tran_loop = False
    else:
        print("transaction code is not correct please try agin")