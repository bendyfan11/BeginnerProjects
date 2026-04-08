#Email Validator Doohicky
import re
Email = input("What is your email?")
Valid = r"^([A-Za-z0-9._%+-])+@([A-Za-z0-9.-])+\.+([a-zA-Z]{2,})$"
if re.fullmatch(valid, email):
  print("This is a valid Email.")
else:
  print(f"Error. Expected format: X@X.x. Got {Email}.)
