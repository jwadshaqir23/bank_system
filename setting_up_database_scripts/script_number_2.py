import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent"
)
mycursor = mydb.cursor()
db_name2 = "history_bank"
mycursor.execute(f"CREATE DATABASE {db_name2}")

mydb.close()

mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="history_bank"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE agent1_history_pos (how_much VARCHAR(65535), reason VARCHAR(65535), from_who VARCHAR(65535),date VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent1_tran (recivier VARCHAR(65535), how_much VARCHAR(65535), acc_num VARCHAR(65535), reason VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent1_minus (how_much VARCHAR(65535), reason VARCHAR(65535), who_pos_to VARCHAR(65535), date VARCHAR(65535))")

#########################
mycursor.execute("CREATE TABLE agent23_history_pos (how_much VARCHAR(65535), reason VARCHAR(65535), from_who VARCHAR(65535),date VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent23_tran (recivier VARCHAR(65535), how_much VARCHAR(65535), acc_num VARCHAR(65535), reason VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent23_minus (how_much VARCHAR(65535), reason VARCHAR(65535), who_pos_to VARCHAR(65535), date VARCHAR(65535))")
##############################
mycursor.execute("CREATE TABLE agent268_history_pos (how_much VARCHAR(65535), reason VARCHAR(65535), from_who VARCHAR(65535),date VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent268_tran (recivier VARCHAR(65535), how_much VARCHAR(65535), acc_num VARCHAR(65535), reason VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent268_minus (how_much VARCHAR(65535), reason VARCHAR(65535), who_pos_to VARCHAR(65535), date VARCHAR(65535))")
##############################
mycursor.execute("CREATE TABLE agent2_history_pos (how_much VARCHAR(65535), reason VARCHAR(65535), from_who VARCHAR(65535),date VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent2_tran (recivier VARCHAR(65535), how_much VARCHAR(65535), acc_num VARCHAR(65535), reason VARCHAR(65535))")
mycursor.execute("CREATE TABLE agent2_minus (how_much VARCHAR(65535), reason VARCHAR(65535), who_pos_to VARCHAR(65535), date VARCHAR(65535))")




