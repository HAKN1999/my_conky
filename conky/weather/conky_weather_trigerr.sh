#!/bin/bash
sleep 4

#bash $HOME/.config/conky/ &
python ~/.config/conky/weather/weather_pull.py &

sleep 1

conky -d -c ~/.config/conky/weather/conky_weather.conf &
