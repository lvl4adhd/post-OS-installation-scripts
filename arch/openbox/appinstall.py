# Module(s)
import os


# Function(s)
def cmd(command):
    os.system(command)


# Getting app listt and links
listt_open = open("listt.txt", "r")
listt_read = listt_open.read()  # you must read the file before splitting it
listt = listt_read.split("\n")


# Printing a readable listt for the user
dict = {}
index = 1
total_apps = len(listt)

while index <= total_apps:
    for data in listt:
        split = data.split(":")
        app = split[0]
        dict[str(index)] = data
        print(f"[{index}]{app}")
        index += 1


# Installing user selected package
print("\nEnter the index of the apps you want to install")
print("Separate multiple options by a semicolon!")
print("!!! NOT INSTALLING THE ESSENTIALS FIRST MAY CAUSE PROBLEM IN FURTHER SETUP PROCESS !!!")
print("Write 'a' to install all packages")
selection = input("\n> ")
selection_listt = selection.split(";")

if selection == 'a' or selection == 'A':
    for data in listt:
        split = data.split(":")
        inst_cmd = split[1]
        cmd(inst_cmd)
        exit()

for indexx in selection_listt:
    if int(indexx) > total_apps:
        print('Invalid Choice!')
        exit()
    extracted_appdata = dict[indexx]
    extracted_appdata_split = extracted_appdata.split(":")
    inst_cmd = extracted_appdata_split[1]
    cmd(inst_cmd)