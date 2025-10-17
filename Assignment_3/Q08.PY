userid='address'
password='1234'
import random 
username=input("enter the username:")
passw=input("enter the password:")
if (username==userid and passw==password):
    captcha=random. randint(1000,9999)
    print("captcha number is:", captcha)
    user_captcha= int(input("enter captcha shown above:"))
    if user_captcha==captcha:
        print("login successfully..")
    else:
        print("captcha wrong..")
else:
    print("invalid userid and password..")
    