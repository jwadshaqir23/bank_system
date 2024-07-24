import os
import importlib

choose_loop = True
def menu():
    #
  print("1;view balance")
  print("2;send money")
  print("3;request money")
  print("4;view history")

  choose = input(">>>")
  choose1_used_for_first_time = False
  choose2_used_for_first_time = False
  choose3_used_for_first_time = False
  choose4_used_for_first_time = False
  if choose == "1":
      from scripts.view_balance import start_view_balance
      start_view_balance()
      input("hit any key to continue")
      os.system("cls")
  elif choose == "2":
      from scripts.send_money_system import start_send_money_system
      start_send_money_system()
      input("hit any key to continue")
      os.system("cls")
  elif choose == "3":
      from scripts.request_money_system import start_request_money_system
      start_request_money_system()
      input("hit any key to continue")
      os.system("cls")
  elif choose == "4":
      from scripts.view_history import start_view_history
      start_view_history()
      input("hit any key to continue")
      os.system("cls")
  else:
      print("undefined input ,try agin")
      input("hit any key to continue")
      os.system("cls")


while choose_loop:
    menu()