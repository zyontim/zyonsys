import getpass
import os
password = "471781692305797955"

attempt = getpass.getpass("Enter your password: ")

if attempt == password:
    print("Access granted.")
else:
    print("Access denied")