#!/bin/bash
sudo pacman -U *.pkg.tar.zst
sudo pacman -S discord steam google-chrome dropbox python-pip vlc pamac-aur nemo libreoffice-still obs-studio
pip install flake8
pamac remove dolphin-plugins
pamac remove kde-servicemenus-rootactions
pamac remove dolphin
sudo pacman -R firedragon-extension-plasma-integration firedragon
