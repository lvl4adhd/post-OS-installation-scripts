import os

def cmd(command):
    os.system("{}".format(command))

cmd("sudo pacman -S pulseaudio pulseaudio-alsa pulseaudio-bluetooth kmix pasystray sof-firmware alsa-firmware")
cmd("sudo pacman -S bluez bluez-utils pulseaudio-bluetooth bluedevil; modprobe btusb; systemctl enable bluetooth.service; systemctl start bluetooth.service")