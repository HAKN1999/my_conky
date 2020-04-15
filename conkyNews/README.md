# requirements
--plank
sudo apt instll plank

# copy font 
sudo cp fonts/* /usr/share/fonts

# copy file autostart
cp autostart/* ~/.config/autostart

# copy file .conkyrc
cp .conkyrc ~/

# copy theme plank
sudo cp -r macOS Black Transparency /usr/share/plank/themes/

# activate plank theme
--open terminal
--command
   plank --preferences
 Dibagian opsi theme pilih dengan theme macos black
