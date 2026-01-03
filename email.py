import re

email_condition = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
user_email = input("enter your Email :")
if re.search(email_condition,user_email):
    print("valid email")
else:
    print("invalid email")
# This code checks if the entered email address is valid based on a regex pattern.
