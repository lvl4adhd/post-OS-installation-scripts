#!/bin/bash
sudo pacman -Sy
sudo pacman -Syu
sudo pacman -U *.pkg.tar.zst
sudo pacman -S discord steam
sudo pacman -S nautilus-dropbox gnome-tweaks gnome-shell-extension-manager python3-pip
pip install flake8
sudo pacman -S chrome-gnome-shell
