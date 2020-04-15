# conky
 
# --BUG
     Masih terdapat Bug di autostart untuk tampilan weather

# --Requirement
    --vnstat 
    sudo apt install vnstat

# --Configurasi
    cd conky/ 
    ./install_conky.py
    --copy font 
    sudo cp fonts/* /usr/share/fonts

# --Configurasi file vnstat 
    /etc/vnstat.conf dengan perangkat jaringan yang di gunakan enp4s0/wlp3s0?:

# --Trial tampilan
    sudo killall conky
    conky
    --untuk menjalankan weather
    cd weather/
    sh conky_weather_trigerr.sh

# --Untuk set posisi
    --masuk di weather/conky_weather.conf
    --rubah nilai gap_x,gap_y
    gap_x = 450,
    gap_y = 522,
    
# --Credits
     Many thanks to :
          @Kosteron
           - https://github.com/Kosteron/Conky
