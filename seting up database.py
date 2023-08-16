import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent"
)
mycursor = mydb.cursor()

db_name1 = "bank_system"
mycursor.execute(f"CREATE DATABASE {db_name1}")

mydb.commit()
mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system"
)

mycursor.execute("CREATE TABLE login_system (username VARCHAR(9999999), password VARCHAR(9999999), actual_name VARCHAR(9999999),gender VARCHAR(9999999), email VARCHAR(9999999))")
mycursor.execute("CREATE TABLE bank_accounts_info (username VARCHAR(9999999), balance VARCHAR(9999999))")
mycursor.execute("CREATE TABLE req_mon_cod (username VARCHAR(9999999), req_code VARCHAR(9999999), code_open_date VARCHAR(9999999))")

mydb.commit()

sql = "INSERT INTO login_system (username, password, actual_name, gender , email) VALUES (%s, %s,%s, %s,%s)"
val = ('agent1','agent109876','real agent','men','agent@email.com')
mycursor.execute(sql, val)

sql = "INSERT INTO login_system (username, password, actual_name, gender , email) VALUES (%s, %s,%s, %s,%s)"
val = ('agent23','agent109876','real agent','women','agent243@email.com')
mycursor.execute(sql, val)

sql = "INSERT INTO login_system (username, password, actual_name, gender , email) VALUES (%s, %s,%s, %s,%s)"
val = ('agent268','agent109876','real agent','men','agent22@email.com')
mycursor.execute(sql, val)


sql = "INSERT INTO login_system (username, password, actual_name, gender , email) VALUES (%s, %s,%s, %s,%s)"
val = ('agent2','agent109876','real agent','women','agent887@email.com')
mycursor.execute(sql, val)


mydb.commit()

sql = "INSERT INTO bank_account_info (username, balance) VALUES (%s, %s)"
val = ('agent1','15000')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_account_info (username, balance) VALUES (%s, %s)"
val = ('agent23','2764')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_account_info (username, balance) VALUES (%s, %s)"
val = ('agent268','-3405')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_account_info (username, balance) VALUES (%s, %s)"
val = ('agent2','25000')
mycursor.execute(sql, val)

mydb.commit()

mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent"
)
db_name2 = "history_bank"
mycursor.execute(f"CREATE DATABASE {db_name2}")

mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="history_bank"
)

mycursor.execute("CREATE TABLE agent1_history_pos (how_much VARCHAR(9999999), reason VARCHAR(9999999), from_who VARCHAR(9999999),date VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent1_tran (recivier VARCHAR(9999999), how_much VARCHAR(9999999), acc_num VARCHAR(9999999), reason VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent1_minus (how_much VARCHAR(9999999), reason VARCHAR(9999999), who_pos_to VARCHAR(9999999), date VARCHAR(9999999))")

#########################
mycursor.execute("CREATE TABLE agent23_history_pos (how_much VARCHAR(9999999), reason VARCHAR(9999999), from_who VARCHAR(9999999),date VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent23_tran (recivier VARCHAR(9999999), how_much VARCHAR(9999999), acc_num VARCHAR(9999999), reason VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent23_minus (how_much VARCHAR(9999999), reason VARCHAR(9999999), who_pos_to VARCHAR(9999999), date VARCHAR(9999999))")
##############################
mycursor.execute("CREATE TABLE agent268_history_pos (how_much VARCHAR(9999999), reason VARCHAR(9999999), from_who VARCHAR(9999999),date VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent268_tran (recivier VARCHAR(9999999), how_much VARCHAR(9999999), acc_num VARCHAR(9999999), reason VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent268_minus (how_much VARCHAR(9999999), reason VARCHAR(9999999), who_pos_to VARCHAR(9999999), date VARCHAR(9999999))")
##############################
mycursor.execute("CREATE TABLE agent2_history_pos (how_much VARCHAR(9999999), reason VARCHAR(9999999), from_who VARCHAR(9999999),date VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent2_tran (recivier VARCHAR(9999999), how_much VARCHAR(9999999), acc_num VARCHAR(9999999), reason VARCHAR(9999999))")
mycursor.execute("CREATE TABLE agent2_minus (how_much VARCHAR(9999999), reason VARCHAR(9999999), who_pos_to VARCHAR(9999999), date VARCHAR(9999999))")




