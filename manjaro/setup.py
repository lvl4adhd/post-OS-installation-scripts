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
cmd("sudo pacman -Sy")
cmd("sudo pacman -Syu")
cmd("sudo pacman -U *.pkg.tar.zst")
cmd("chmod a+x *.sh")
for choice in choice_list:
    match choice:
        case "1":
            cmd("sudo pacman -S discord")
        case '2':
            cmd("sudo pacman -S steam")
        case '3':
            cmd("sudo pacman -S nautilus-dropbox")
        case '4':
            cmd("sudo pacman -S gnome-tweaks")
            cmd("sudo pacman -S chrome-gnome-shell")
        case '5':
            cmd("sudo pacman -S gnome-shell-extention-manager")
        case '6':
            cmd("sudo pacman -S python3-pip")
        case '7':
            cmd("sudo pacman -S python3-pip")
            cmd("pip3 install flake8")
        case "all":
            cmd("./all.sh")
        case "All":
            cmd("./all.sh")
        case _:
            print("Invalid choice!")

