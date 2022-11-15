#Multifunctional Counting Program

from rich.table import Table
from rich import print as rcprint
from time import sleep
import os

#globals
global calctype
global calcsym 
global menu

#pick type
calctype = Table()
calctype.add_column("Select a Type:")
calctype.add_row("1. Integer/Numbers")
calctype.add_row("2. Floats/Decimals")
calctype.add_row("3. Return")

#select symbol
calcsym = Table()
calcsym.add_column("Choose a Sign:")
calcsym.add_row("1. Addition (+)")
calcsym.add_row("2. Subtraction (-)")
calcsym.add_row("3. Multiplication (*)")
calcsym.add_row("4. Division (/)")
calcsym.add_row("5. Modulus (%)")
calcsym.add_row("6. Exponent (**)")
calcsym.add_row("7. Floor Division(//)")

#main menu
menu = Table()
menu.add_column("M A I N  M E N U")
menu.add_row("1. Calculator")
menu.add_row("2. Weight Calculator")
menu.add_row("3. Exit")

def mainmenu():

    #no edit
    name = "Multifunctional Counting Program"
    ver = "[#FFFF00]v1.2[/#FFFF00],"
    compdate = "11-1-22\n"

    clear()
    rcprint(name, ver, "Compile Date:", compdate)
    rcprint(menu)
    typec = input("> ")
    if typec == "1":
        calc()
    elif typec == "2":
        weightcalc()
    elif typec == "3":
        exitprog()
    else:
        print("Invalid Input, Please try again")
        print("Press ENTER to continue....")
        input()
        mainmenu()

def weightcalc():
    clear()
    weight = int(input("Input Weight: "))
    typw = input("Is the weight in KG or LBS? K = KG, L = LBS\n> ")

    clear()
    if typw == "K" or typw == "k":
        weightk = weight * 2.21
        print("Your KG in LBS:", weightk)
        endw = input("Would you like to calculate again? (Y/N)\n> ")
        if endw == "y" or endw == "Y":
            weightcalc()
        elif endw == "n" or endw == "N":
            mainmenu()
        else:
            exit()
    elif typw == "L" or typw == "l":
        weightl = weight * 0.45
        print("Your LBS in KG:", weightl)
        endw = input("Would you like to calculate again? (Y/N)\n> ")
        if endw == "y" or endw == "Y":
            weightcalc()
        elif endw == "n" or endw == "N":
            mainmenu()
        else:
            exit()
    else:
        print("Wrong Input, Please Try again.")
        print("Press ENTER to Continue....")
        input()
        weightcalc()
    
def calc():
    clear()
    rcprint(calctype)
    typec = input("> ")
    if typec == "1":
        calcint()
    elif typec == "2":
        calcflo()
    elif typec == "3":
        mainmenu()
    else:
        print("Invalid Input, Please try again")
        print("Press ENTER to continue....")
        input()
        mainmenu()


def calcint():
    clear()
    num1 = int(input("Input First number: (INT)\n> "))
    clear()
    num2 = int(input("Input Second number: (INT)\n> "))
    clear()
    rcprint(calcsym)
    symbol = input("> ")
    clear()

    if symbol == "1":
        print("Your Result is: ")
        print(num1 + num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "2":
        print("Your Result is: ")
        print(num1 - num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "3":
        print("Your Result is: ")
        print(num1 * num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "4":
        print("Your Result on a int is: ")
        print(int(num1 / num2))
        print("Your Result on a float is:")
        print(num1 / num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "5":
        print("Your Result is: ")
        print(num1 % num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "6":
        print("Your Result is: ")
        print(num1 ** num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "7":
        print("Your Result is: ")
        print(num1 // num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    else: 
        print("Invalid Input, Please try again")
        print("Press ENTER to continue....")
        input()
        calcint()

def calcflo():
    clear()
    num1 = float(input("Input First number: (FLOAT)\n> "))
    clear()
    num2 = float(input("Input Second number: (FLOAT)\n> "))
    clear()
    rcprint(calcsym)
    symbol = input("> ")

    if symbol == "1":
        print("Your Result is: ")
        print(num1 + num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "2":
        print("Your Result is: ")
        print(num1 - num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "3":
        print("Your Result is: ")
        print(num1 * num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "4":
        print("Your Result on a int is: ")
        print(int(num1 / num2))
        print("Your Result on a float is:")
        print(num1 / num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "5":
        print("Your Result is: ")
        print(num1 % num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "6":
        print("Your Result is: ")
        print(num1 ** num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    elif symbol == "7":
        print("Your Result is: ")
        print(num1 // num2)
        print("Would You like to Calculate Again? (Y/N)")
        end = input("> ")
        if end == "y" or end == "Y":
            calc()
        elif end == "n" or end == "N":
            mainmenu()
        else:
            exit()
    else: 
        print("Invalid Input, Please try again")
        print("Press ENTER to continue....")
        input()
        calcflo()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def exitprog():
    clear()
    rcprint("[bright_red]Closing app...[/bright_red]")
    sleep(3)
    rcprint("[#FFA500]Its now safe to turn off your console.[/#FFA500]")
    sleep(2)

mainmenu()