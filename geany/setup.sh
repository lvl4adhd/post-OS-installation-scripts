#!/bin/bash
echo --------------------------------------------
echo Installing geany and vte...
sudo pacman -S geany vte3 vte4
echo --------------------------------------------
echo Restoring your configurations...
cp -r geany ~/.config/
echo --------------------------------------------
echo Done!
