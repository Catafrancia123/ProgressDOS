from rich import print as printr
from rich.progress import track
from time import sleep as delay
from cls import clear
import socket as chknet
import speedtest as chkspd
import webbrowser as web


def eastereggs(name):
    if name == "helloworld":
        clear()
        printr("[bright_yellow]EASTER EGG #1[/bright_yellow]\n")
        print("Hello World!")
        print("the famous line that started the programming history!")
        print("Press ENTER to Continue....")
        input()

def achivementsave(achivement, trueorfalse):
    openfile = open("achvsave.txt", "w")

    if trueorfalse == "true":
        openfile.write(achivement)
        openfile.write(": true")
    elif trueorfalse == "false":
        openfile.write(achivement)
        openfile.write(": false")

def checknetwrk(link):
    try:
        s = chknet.create_connection(
              (link, 80))
        if s is not None:
            s.close
        return True
    except OSError:
        pass
    return False

def network():
    computername = chknet.gethostname()
    computerip = chknet.gethostbyname(computername)

    for coninter in track(range(100), description='[green]Connecting to Internet...'):
        delay(0.10)

        if coninter == 10:
            net = checknetwrk("www.google.com")

            if net == True:
                continue
            elif net == False:
                track(disable=True)
                clear()
                print("Your computer has not been connected to the internet.\nHalting Operation...")
                delay(3)
                clear()
        elif coninter == 30:
            print("Computer Name:", computername)
        elif coninter == 60:
            print("IP Address:", computerip)
    printr("[bright_yellow]Connection Established[/bright_yellow].")

def chkspeed():
    printr("[bright_yellow]Please Wait...[/bright_yellow]")
    speed = chkspd.Speedtest()
    spdd = speed.download()
    spdu = speed.upload()
    server = []
    speed.get_servers(server)
    spdp = speed.results.ping
        
    printr("[#7600bc]\nDownload Speed[/#7600bc]:", spdd, "MB/s")
    printr("[green]Upload Speed[/green]:", spdu, "MB/s")
    printr("[cyan]Ping Speed[/cyan]:", spdp, "ms")

def links(goto):
    if goto == "server":
        printr("[bright_yellow]Redirecting...[/bright_yellow]")
        delay(2)
        web.open_new_tab("https://discord.gg/7S9buXeUMM")
    elif goto == "help":
        printr("[bright_yellow]Redirecting...[/bright_yellow]")
        delay(2)
        web.open_new_tab("https://github.com/Catafrancia123/ProgressDOS")
    else:
        raise NameError("Link not found. Make sure your typing it correctly")