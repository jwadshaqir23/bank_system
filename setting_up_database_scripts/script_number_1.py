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
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE login_system (username VARCHAR(65535), password VARCHAR(65535), actual_name VARCHAR(65535),gender VARCHAR(65535), email VARCHAR(65535))")
mycursor.execute("CREATE TABLE bank_accounts_info (username VARCHAR(65535), balance VARCHAR(65535))")
mycursor.execute("CREATE TABLE req_mon_cod (username VARCHAR(65535), req_code VARCHAR(65535), code_open_date VARCHAR(65535))")

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

sql = "INSERT INTO bank_accounts_info (username, balance) VALUES (%s, %s)"
val = ('agent1','15000')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_accounts_info (username, balance) VALUES (%s, %s)"
val = ('agent23','2764')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_accounts_info (username, balance) VALUES (%s, %s)"
val = ('agent268','-3405')
mycursor.execute(sql, val)

sql = "INSERT INTO bank_accounts_info (username, balance) VALUES (%s, %s)"
val = ('agent2','25000')
mycursor.execute(sql, val)

mydb.commit()

mydb.close()