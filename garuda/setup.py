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
[4] Pip
[5] Flake8 (Will install [4])
[6] Chrome
[7] Nemo file explorer
[8] OBS Studio
[9] Libre Office""")

print("""Enter the number beside the package you want to install.
Every number must be seperated by a space.
Write "All" for installing all packages""")

choice_ = input("\nChoice> ")
print("----------------------------------------------")


# Installation...
choice_list = choice_.split(" ")
cmd("sudo pacman -Sy")
cmd("sudo garuda-update")
cmd("sudo pacman -U *.pkg.tar.zst")
cmd("chmod a+x all.sh")
for choice in choice_list:
    match choice:
        case "1":
            cmd("sudo pacman -S discord")
        case '2':
            cmd("sudo pacman -S steam")
        case '3':
            cmd("sudo pacman -S dropbox")
        case '4':
            cmd("sudo pacman -S python-pip")
        case '5':
            cmd("sudo pacman -S python-pip")
            cmd("pip install flake8")
        case '6':
            cmd("sudo pacman -S google-chrome")
            cmd("sudo pacman -R firedragon-extension-plasma-integration firedragon")
        case '7':
            cmd("sudo pacman -S pamac-aur")
            cmd("sudo pacman -S nemo")
            cmd("pamac remove dolphin-plugins")
            cmd("pamac remove kde-servicemenus-rootactions")
            cmd("pamac remove dolphin")
        case '8':
            cmd("sudo pacman -S obs-studio")
        case '9':
            cmd("sudo pacman -S libreoffice-still")
        case "all":
            cmd("bash all.sh")
        case "All":
            cmd("bash all.sh")
        case _:
            print("Invalid choice!")

