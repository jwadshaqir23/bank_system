print("welcome to the verfiy system")
print("please select the way you need to verfiy your self")
print("1;email verfying")

loop = True
while loop:
    #
    type_choose = input(">>>")

    if type_choose == "1":
        import os
        os.system("cls")
        import scripts.verfying_system.email_verfiy
        loop = False
        os.system("cls")

