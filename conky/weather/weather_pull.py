#!/usr/bin/python

from os.path import expanduser
import os
import time

home = expanduser("~")

loc_default_conky = "${offset 1150}${color royal blue}${exec cat ~/.config/conky/weather/weather.tmp}\n"
loc_update_tmp = "${offset 1150}${color dark cyan}${exec cat /tmp/weather.tmp}\n"


def weather_pull(location):
    while True:
        #  datapatkan prakira cuaca dan simpan ke weather.tmp
        # jika ada internet ini akan diperbaharui
        os.system(
            'curl "http://id.wttr.in/{location}?T&1&F&" --silent --max-time 3 > /tmp/weather.tmp'.format(location=location))
        # baca panjang karakter dan jika == 0 berarti tidak di perbaharui atau tidak ada internet
        with open("/tmp/weather.tmp", "r") as f:
            lenght_text = len(f.read())

            # jika panjang karakter > 0 gunakan file weather.tmp  di folder /tmp {uptodate}
        if lenght_text > 0:
            # jika ada interntet folder path di ganti ke /tmp {uptodate} dan update file weather.tmp  
            # di folder conky/weather
            # file lama
            write_to_spesific(loc_update_tmp)
            # untuk mempetahankan jika koneksi internet tidak ada di file weather.tmp conky/weather
            # tidak di replace ke file kosong dan ttp di tampilkan yg lama
            # update file weather.tmp di folder conky/weather jika ada internet
            os.system(
                'curl "http://id.wttr.in/{location}?T&1&F&" --silent --max-time 3 >  ~/.config/conky/weather/weather.tmp'.format(location=location))

            # jika panjang karakter == 0 gunakan file weather.tmp di folder conky/weather {kurang diperbaharui}
        if lenght_text == 0:
            write_to_spesific(loc_default_conky)
            # durasi pembaruan
        time.sleep(1800)


def write_to_spesific(location):
    # baca file conky config
    with open("{home}/.config/conky/weather/conky_weather.conf".format(home=home), "r") as f:
        read_text = f.readlines()

    #  dapatkan index yg akan di replace dengan kententuan jika ada internet menggunakna /tmp dan 
    #  tidak menggunakan conky/weather
    write_text = read_text
    write_text[41] = "{location}".format(location=location)

    # jika file tidak ada buat file dan simpan hasil perubahan dari write_text[index]
    pj1 = len(write_text)

    with open("{home}/.config/conky/weather/conky_weather.conf".format(home=home), "w") as f2:
        #  menggunkan loop untuk menulis ulang
        for i in range(0, pj1):
            f2.write(write_text[i])


def main():

    location = "-8.148291,%20112.33509"
    weather_pull(location)


if __name__ == "__main__":
    main()
