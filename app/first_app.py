import login_system
from login_system import login_system_loop_passing
import os
os.system("cls")
if login_system_loop_passing == True:
    import verfiy_system
    from scripts.verfying_system.email_verfiy import verfiy_code_number
    verfiy_code = input("your verfiy code that in your email:")
    if verfiy_code == verfiy_code_number:
        verfiy_system_pass = "yes"
        print("you passed the verfiy")
        import scripts.gender_check
        from scripts.gender_check import is_the_user_men
        from scripts.gender_check import is_the_user_women
        from scripts.get_user_actual_name import user_actual_name
        if is_the_user_men == True:
            os.system("cls")
            welcome_print = print("welcome mr."+user_actual_name)
            import main_app

        if is_the_user_women == True:
            os.system("cls")
            welcome_print = print("welcome mis."+user_actual_name)
            import main_app

