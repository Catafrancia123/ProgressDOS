#SETUP PROGRAM

from time import sleep as delay
import os

def setup():
    clear()
    print("Welcome to ProgressDOS Package Setup!")
    print("Press ENTER to continue....")
    input()
    setupdep()

def setupdep():
    clear()
    os.system("pip install -i https://test.pypi.org/simple/ cls-en")
    delay(1)
    os.system("pip install rich")
    delay(1)
    os.system("pip install speedtest-cli")
    delay(1)
    setupend()

def setupend():
    clear()
    print("Setup has completed Install.")
    delay(3)
    
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

setup()