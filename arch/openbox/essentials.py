import os

def cmd(command):
    os.system("{}".format(command))

# YAY
cmd("sudo pacman -S --needed base-devel git")
cmd("git clone https://aur.archlinux.org/yay-bin.git")
cmd("cd yay-bin && makepkg -si")
cmd("yay -Y --gendb")
cmd("yay -Syu --devel")
cmd("yay -Y --devel --save")
cmd("rm -r yay-bin")

# Printer
cmd("sudo pacman -Syu cups hplip system-config-printer gtk3-print-backends")
cmd("sudo hp-setup -i")

# Others
