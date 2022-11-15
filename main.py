#ProgressbarDOS

from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich import print as printr
from cls import clear
from dirs import dircmd as dir
from extras import *
from time import sleep as delay
from os.path import exists
from os import startfile as run

#globals
global helpmenu
global credstable

#tables
#helpmenu
helpmenu = Table(title="Commands")
helpmenu.add_column("No.", style="blue", no_wrap=True)
helpmenu.add_column("Command Name", style="bright_green")
helpmenu.add_column("Run Command", style="bright_yellow", justify="left")

helpmenu.add_row("1", "Clear the screen", "clear")
helpmenu.add_row("2", "Exit console", "exit")
helpmenu.add_row("3", "Running Programs", "run(program run name)")
helpmenu.add_row("4", "Display files inside a Directory", "dir")
helpmenu.add_row("5", "Go to a directory", "gtd(dir name)")
helpmenu.add_row("6", "Go back to parent directory", "dirout")
helpmenu.add_row("7", "Help Menu", "help")
helpmenu.add_row("8", "Credits", "creds/credits")
helpmenu.add_row("9", "Show Version", "ver")
helpmenu.add_row("10", "See Achivements", "achv")
helpmenu.add_row("11", "Printing a String", "printl(your text)")
helpmenu.add_row("12", "Our Discord Server", "pbserver")
helpmenu.add_row("13", "Help on Development", "pbhelp")
helpmenu.add_row("14", "Connect to the internet", "net")
helpmenu.add_row("15", "Check Internet Speed", "netspeed")

#credits
credstable = Table(title="ProgressDOS Team/Helpers", caption="If you want to help, say 'pbhelp' to go the repo.")
credstable.add_column("No.", style="blue", no_wrap=True)
credstable.add_column("Name", style="bright_yellow")
credstable.add_column("Github Name", style="#bd2c00")
credstable.add_column("Origin of Server", justify="center")

credstable.add_row("1", "Kyle", "Catafrancia123", "[#5ed3ff]Progressbar Community Discord Server[/#5ed3ff]")
credstable.add_row("2", "Alexandros", "lxndroc", "[#FFEF00]Build Your Dream Python Project[/#FFEF00]" )
credstable.add_row("3", "Vlad", "biscuitdelicious", "[#F7751B]Coding & Programming with Matt Upham[/#F7751B]")

def dos():
    menu = input("\npbsys:> ")
    if menu == "help":
        helpmesnu()
        dos()
    elif menu == "":
        dos()
    elif menu == "clear":
        clear()
        dos()
    elif menu.split()[0] == "printl":
        delcmd = menu.replace("printl ", "")
        print(delcmd)
        dos()
    elif menu == "dir" or menu == "DIR":
        dir("dos")
        dos()
    elif menu == "exit":
        exit()
    elif menu == "gtdProgressbar":
        progressbar()
    elif menu == "gtdGames":
        games()
    elif menu == "gtdDocuments":
        documents()
    elif menu == "hello" or menu == "Hello":
        clear()
        eastereggs("helloworld")
        achivementsave("helloworld", "true")
        dos()
    elif menu == "creds" or menu == "credits":
        creds()
        dos()
    elif menu == "achv":
        achivements()
    elif menu == "ver":
        clear()
        dosinfo()
        dos()
    elif menu == "pbserver":
        links("server")
        dos()
    elif menu == "pbhelp":
        links("help")
        dos()
    elif menu == "runreadme":
        clear()
        openfile = open("progressbar/README.txt", "r")
        readme = openfile.read()

        print(readme)
        print("\nPress ENTER to continue...")
        input()
        dos()
    elif menu == "net":
        network()
        dos()
    elif menu == "netspeed":
        chkspeed()
        dos()
       
    else:
        print("'"+menu+"'", "is not recognized as a file or a Command.")
        dos()

def helpmesnu():
    clear()
    printr(helpmenu)
    printr("[bright_yellow]This DOS prompt has also Easter Eggs! Good luck finding![/bright_yellow]")
    print("Press ENTER to Continue....")
    input()

def creds():
    clear()
    printr(credstable)
    print("\nPress ENTER to continue....")
    input()

def welcome():
    clear()
    welcome.counter += 1
    print("user calls:", welcome.counter)
    clear()
    welcomefunc()
welcome.counter = 0

def welcomefunc():
    if welcome.counter == 1:
        dosinfo()
    elif welcome.counter > 1:
        dos()
    else:
        exit()

def achivements():
    clear()
    openfile = open("achvsave.txt", 'r')
    achv = openfile.read()

    print(achv)
    print("Press ENTER to continue...")
    input()
    dos()

def checkachvsave():
    clear()
    saveexist = exists("achvsave.txt")

    if saveexist == True:
        print("Achivements save file detected.")
        delay(0.1)
        welcome()
    elif saveexist == False:
        open("achvsave.txt", "x")
        checkachvsave()

def documents():
    menu = input("\npbsys\Documents:> ")
    if menu == "dirout":
        dos()
    elif menu == "dir" or menu == "DIR":
        dir("documents")
        documents()
    elif menu == "help":
        helpmesnu()
        documents()
    elif menu == "runcalc":
        open("documents\pycalc.py")
        documents()
    elif menu == "clear":
        clear()
        documents()
    elif menu == "exit":
        exit()
    elif menu == "pbserver":
        links("server")
        documents()
    elif menu == "pbhelp":
        links("help")
        documents()
    elif menu.split()[0] == "printl":
        delcmd = menu.replace("printl ", "")
        print(delcmd)
        games()
    elif menu == "hello" or menu == "Hello":
        clear()
        eastereggs("helloworld")
        achivementsave("helloworld", "true")
        documents()
    elif menu == "creds" or menu == "credits":
        creds()
        documents()
    else:
        print("'"+menu+"'", "is not recognized as a file or a Command.")
        documents()

def dosinfo():
    #no touch!!
    ver = "[bright_yellow]v0.1[/bright_yellow],"
    compdate = "[red]11-13-2022[/red]"
    progressbar = "[#72bcd4]Prog[/#72bcd4][#FFA500]ress[/#FFA500][#EE4B2B]bar[/#EE4B2B]"
    discord = "[#7289da]Discord Server[/#7289da]"
    cprydate = "2022-2022"
    pbdos = "ProgressDOS"

    printr(pbdos, ver, "Compile Date:", compdate)
    printr("[bright_yellow](c)[/bright_yellow]", progressbar, discord, cprydate, "All rights Reserved.")
    dos()

def progressbar():
    menu = input("\npbsys\Progressbar:> ")
    if menu == "dirout":
        dos()
    elif menu == "dir" or menu == "DIR":
        dir("pb")
        progressbar()
    elif menu == "help":
        helpmesnu()
        progressbar()
    elif menu == "clear":
        clear()
        progressbar()
    elif menu == "runreadsys":
        clear()
        openfile = open("progressbar/READSYS.txt", "r")
        readsys = openfile.read()

        print(readsys)
        print("\nPress ENTER to continue...")
        input()
        progressbar()
    elif menu.split()[0] == "printl":
        delcmd = menu.replace("printl ", "")
        print(delcmd)
        progressbar()
    else:
        print("'"+menu+"'", "is not recognized as a file or a Command.")
        progressbar()

def games():
    menu = input("\npbsys\Games:> ")
    if menu.split()[0] == "printl":
        delcmd = menu.replace("printl ", "")
        print(delcmd)
        games()
    elif menu == "help":
        helpmesnu()
        games()
    elif menu == "clear":
        clear()
        games()
    elif menu == "dir" or menu == "DIR":
        dir("games")
        games()
    elif menu == "exit":
        exit()
    elif menu == "dirout":
        dos()
    elif menu == "creds" or menu == "credits":
        creds()
        games()
    elif menu == 'dos' or menu == "pb":
        clear()
        dosinfo()
        games()
    elif menu == "pbserver":
        links("server")
        games()
    elif menu == "pbhelp":
        links("help")
        games()
    else:
        print("'"+menu+"'", "is not recognized as a file or a Command.")
        games()

checkachvsave()