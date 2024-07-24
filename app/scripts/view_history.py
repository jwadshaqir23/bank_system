def start_view_history():
    
    from login_system import login_user
    import mysql.connector
    import os
    mydb = mysql.connector.connect(
    host="localhost",
    user="bank_agent",
    password="bank_agent",
    database="history_bank"
    )
    
    mycursor = mydb.cursor()
    def check_if_there_is_history_postive():
        pos = "_history_pos"
        mycursor.execute(f"SELECT EXISTS(SELECT 1 FROM {login_user+pos} LIMIT 1)")
        myresult = mycursor.fetchone()[0]
        return myresult == 1
    def check_if_there_is_history_minus():
        minus = "_minus"
        mycursor.execute(f"SELECT EXISTS(SELECT 1 FROM {login_user+minus} LIMIT 1)")
        myresult = mycursor.fetchone()[0]
        return myresult == 1
    has_data_pos = check_if_there_is_history_postive()
    has_data_minus = check_if_there_is_history_minus()

    os.system("cls")
    print("select what do you want to see")
    print("1;money postives")
    print("2;money miunses")
    print("3;both")

    choose = input(">>>")

    if choose == "1":
        from scripts.history_pos import start_hisotry_pos
    elif choose == "2":
        from scripts.history_minus import start_history_minus
    elif choose == "3":
        if has_data_pos == True:
            from scripts.history_pos import start_hisotry_pos
        elif has_data_pos == False:
            print("there is no any postive history in your account")
        if has_data_minus == True:
            from scripts.history_minus import start_history_minus
        elif has_data_minus == False:
            print("there is no any minus history in your account")
        
    ########################################################################
    # history types: , miuns , postive
    #                    tran       miuns      pos
    # miuns : how many ,reason;prushe withdraw ,tax ,who
    # pos : how many , reason ;salary,deposit ,from who
