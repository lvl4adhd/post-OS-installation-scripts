# Imports
import os


# Functions
def cmd(command: str):
    os.system(f"{command}")


# Package selection
print("----------------------------------------------")

print("""[1] Discord
[2] Steam
[3] Dropbox
[4] GNOME Tweaks (Will install chrome-gnome-shell)
[5] GNOME Shell Extention Manager
[6] Pip
[7] Flake8 (Will install [6])""")

print("""Enter the number beside the package you want to install.
Every number must be seperated by a space.
Write "All" for installing all packages""")

choice_ = input("\nChoice> ")
print("----------------------------------------------")


# Installation...
choice_list = choice_.split(" ")
cmd("sudo apt update")
cmd("sudo apt upgrade")
cmd("sudo dpkg -i *.deb")
for choice in choice_list:
    match choice:
        case "1":
            cmd("sudo snap install discord")
        case '2':
            cmd("sudo snap install steam")
        case '3':
            cmd("sudo apt install nautilus-dropbox")
        case '4':
            cmd("sudo apt install gnome-tweaks")
            cmd("sudo apt-get install chrome-gnome-shell")
        case '5':
            cmd("sudo apt install gnome-shell-extention-manager")
        case '6':
            cmd("sudo apt install python3-pip")
        case '7':
            cmd("sudo apt install python3-pip")
            cmd("pip3 install flake8")
        case "all":
            cmd("./all.sh")
        case "All":
            cmd("./all.sh")
        case _:
            print("Invalid choice!")

