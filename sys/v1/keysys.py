import random
import time
import getpass
import os
from datetime import datetime

print(''' 


██╗░░██╗███████╗██╗░░░██╗  ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗
██║░██╔╝██╔════╝╚██╗░██╔╝  ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║
█████═╝░█████╗░░░╚████╔╝░  ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░  ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║
██║░╚██╗███████╗░░░██║░░░  ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝

  ''')
f = open("credits.txt", "r")
print(f.read(), "\n")
f.close()
key = 471781692305797955 #enter your key here that you want to use for the tool
code = 471781692305797955 #enter your key here that you want to use for the tool
if code != key:
    print("error number 1")
    f = open("ecode1.txt", "r")
    print(f.read(), "\n")
    f.close()
    exit()
else:
    print("You Need to login")
time.sleep(1)
inkey = int(input('Enter your key:'))
if code != inkey:
    print("Invalid Key!","\n")
    f = open("ecode2.txt", "r")
    print(f.read(),"\n")
    f.close()


else:
    print("LOGGED IN", "\n")