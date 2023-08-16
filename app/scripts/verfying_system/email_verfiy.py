import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
#from get_user_email import user_email
import random
import string
letters = string.ascii_lowercase
verfiy_code_number = ''.join(random.choice(letters) for _ in range(4))
#verfiy_code_number =random.randint(1000, 9999)
verfiy_code_number = "25"
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="bank_agent",
  password="bank_agent",
  database="bank_system"
)
mycursor = mydb.cursor()
#from login_system import login_user
from login_system import login_user

mycursor.execute(f"SELECT email FROM login_system WHERE username Like '{login_user}'")
myresult = mycursor.fetchall()
for x_user_email in myresult:
 
 user_email = str(x_user_email[0])

message = Mail(
    from_email='jwad.bank.system1@gmail.com',
    to_emails=user_email,
    subject='jwad bank system verfying email',
    html_content=verfiy_code_number)
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

