from rich.table import Table
from rich.tree import Tree
from rich import print as printr

#globals
global dirdos
global dirdcmts
global dirgames
global dirpb

#tables

#dos directory
dirdos = Table(title="\nContents of pbsys", title_justify="left")
dirdos.add_column("No", style="blue")
dirdos.add_column("File/Directory Name", style="bright_green")
dirdos.add_column("File Run Command Name", style="bright_yellow")
dirdos.add_column("File/Directory Type", style="cyan")

dirdos.add_row("1", "Documents", " ", "DIR")
dirdos.add_row("2", "Games", " ", "DIR")
dirdos.add_row("3", "Progressbar", " ", "DIR")
dirdos.add_row("4", "README", "readme", "TXT")

#documents directory
dirdcmts = Table(title="\nContents of pbsys\Documents", title_justify="left")
dirdcmts.add_column("No", style="blue")
dirdcmts.add_column("File/Directory Name", style="bright_green")
dirdcmts.add_column("File Run Command Name", style="bright_yellow")
dirdcmts.add_column("File/Directory Type", style="cyan")

dirdcmts.add_row("1", "Calculator", "calc", "PBAF")

#games directory
dirgames = Table(title="\nContents of pbsys\Games", title_justify="left")
dirgames.add_column("No", style="blue")
dirgames.add_column("File/Directory Name", style="bright_green")
dirgames.add_column("File Run Command Name", style="bright_yellow")
dirgames.add_column("File/Directory Type", style="cyan")

dirgames.add_row("1", "Guess The Number", "gtn", "PBAF")

#progressbar directory
dirpb = Table(title="\nContents of pbsys\Games", title_justify="left")
dirpb.add_column("No", style="blue")
dirpb.add_column("File/Directory Name", style="bright_green")
dirpb.add_column("File Run Command Name", style="bright_yellow")
dirpb.add_column("File/Directory Type", style="cyan")

dirpb.add_row("1", "ProgressbarOS", " ", "DIR")
dirpb.add_row("2", "sys", " ", "DIR")
dirpb.add_row("3", "sys64", " ", "DIR")
dirpb.add_row("4", "README", "readsys", "TXT")

def dircmd(filedir):
    if filedir == "dos":
        printr(dirdos)
    elif filedir == "documents":
        printr(dirdcmts)
    elif filedir == "games":
        printr(dirgames)
    elif filedir == "pb":
        printr(dirpb)
    else:
        raise NameError("Directory not found. Make sure your typing it correctly")

def fulldir():
    full = Tree("[cyan]pbsys")
    full.add("Progressbar").add("ProgressbarOS")
    full.add("sys").add("sys64")
    full.add("Games")
    full.add("Documents")
    printr(full)

fulldir()

