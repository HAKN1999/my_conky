# Requirements
## Plank
> sudo apt install plank

## conky
> sudo apt install conky-all

# Make dir .conky
> mkdir ~/.conky

# Copy font 
> sudo cp Font/* /usr/share/fonts

# Copy file autostart
> cp conky/conky.desktop ~/.config/autostart

# optional set autostart 
> nano ~/.config/autostart/conky.desktop

> *edit Exec = /home/username/*

# Copy all file conky
> cp conky/* ~/.conky

# Copy theme plank
> sudo cp -r macOS Black Transparency /usr/share/plank/themes/

# Activate plank theme
## Open terminal , command
> plank --preferences 

> Dibagian opsi theme pilih dengan theme macos black
