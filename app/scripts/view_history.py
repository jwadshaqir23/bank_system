from login_system import login_user
pos = "_history_pos"
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="history_bank"
)
mycursor = mydb.cursor()

print("select what do you want to see")
print("1;money postives")
print("2;money miunses")
print("3;both")

choose = input(">>>")

if choose == "1":
    import scripts.history_pos
elif choose == "2":
    import scripts.history_miuns
elif choose == "3":
    import scripts.history_pos
    import scripts.history_miuns
########################################################################
# history types: , miuns , postive
#                    tran       miuns      pos
# miuns : how many ,reason;prushe withdraw ,tax ,who
# pos : how many , reason ;salary,deposit ,from who
