# Module(s)
import os


# Function(s)
def cmd(command):
    os.system(command)


# Installing yay if not installed
print('-------------------------')
print('YAY is required to install some packages')
firsttime = input("Is YAY installed? [y,n]: ")

if firsttime.lower() == 'n':
    cmd("sudo pacman -S --needed base-devel git")
    cmd("git clone https://aur.archlinux.org/yay-bin.git")
    cmd("cd yay-bin && makepkg -si")
    cmd("yay -Y --gendb")
    cmd("yay -Syu --devel")
    cmd("yay -Y --devel --save")

elif firsttime.lower() == 'y':
    pass

else:
    print("Invalid input! Skipping yay installation...")


# Getting app list and links
applist_open = open("applist.txt", "r")
applist_read = applist_open.read()  # you must read the file before splitting it
applist = applist_read.split("\n")


# Printing a readable list for the user
dict = {}
index = 1
total_apps = len(applist)

while index <= total_apps:
    for data in applist:
        split = data.split(":")
        app = split[0]
        dict[str(index)] = data
        print(f"[{index}]{app}")
        index += 1


# Installing user selected package
print("\nEnter the index of the apps you want to install")
print("Separate multiple options by a semicolon!")
print("Write 'a' to install all packages")
selection = input("\n> ")
selection_list = selection.split(";")

if selection == 'a' or selection == 'A':
    for data in applist:
        split = data.split(":")
        inst_cmd = split[1]
        cmd(inst_cmd)
        exit()

for indexx in selection_list:
    if int(indexx) > total_apps:
        print('Invalid Choice!')
        exit()
    extracted_appdata = dict[indexx]
    extracted_appdata_split = extracted_appdata.split(":")
    inst_cmd = extracted_appdata_split[1]
    cmd(inst_cmd)