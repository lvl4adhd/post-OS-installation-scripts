import os

def cmd(command):
    os.system("{}".format(command))

cmd("sudo pacman -Syu cups hplip system-config-printer gtk3-print-backends")
cmd("sudo hp-setup -i")