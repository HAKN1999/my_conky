#!/usr/bin/python
# coding: utf-8

import os
import re
import urllib3
import time
from bs4 import BeautifulSoup
from os.path import expanduser

home = expanduser("~")

loc_default_conky = "${offset 1150}${color royal blue}${exec cat ~/.config/conky/prayer_schd/prayer.tmp}\n"
loc_update_tmp = "${offset 1150}${color dark cyan}${exec cat /tmp/prayer.tmp}\n"


def get_source(url):
    while True:
        try:
            # ambil source code web
            http = urllib3.PoolManager()
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data.decode('utf-8'))
            output = soup
            output = str(output)

            # tampilkan daerah sholat
            daerah_sholats = re.findall(
                r'"nilai">([a-z+A-Z][a-z+A-Z]*.+)<', output)

            # tampilkan title waktu sholat daerah
            title_sholat_daerahs = re.findall(
                r'"title">(\s{10}[A-Z]*)', output)

            # tampilkan waktu sholat daerah
            waktu_sholat_daerahs = re.findall(
                r'"pukul">(\s{10}[0-9:]*)', output)

            # ambil tgl waktu valid informasi
            tgls = re.findall(r'\t{2}var\scurrenttime\s=\s([A-Z]*.+);', output)
            for i in range(0, len(tgls)):  # ektrak tgl di list ke string
                tgls = tgls[i].strip("''")
            fltr = []
            for ii in range(len(tgls)):  # filter string untuk di tampilkan mm/dd/yy
                fltr.append(tgls[ii])
                # print "index %d" % ii,  # pencarian index
                # print fltr[ii:ii+1]
            tgl = "".join(fltr[0:17])

            # ektrak title_sholat_daerah list,hapus \t
            titles = []
            for title_sholat_daerah in range(len(title_sholat_daerahs)):
                titles.append(
                    title_sholat_daerahs[title_sholat_daerah].strip())

            # ektrak waktu_sholat_daerah
            pukuls = []
            for waktu_sholat_daerah in range(len(waktu_sholat_daerahs)):
                pukuls.append(
                    waktu_sholat_daerahs[waktu_sholat_daerah].strip())

            # masukan ke tabel
            tables = """
            {tgl}
            ┌{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}{grsL}{grsD}
            │{tT}│
            ┼{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}{grsL}{grsPl}
            │{pK}│
            └{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}{grsL}{grsU}
            {lok}
            """.format(
                tgl=tgl,
                grsL=8 * "─",
                tT="│".join(str(title).center(8, " ") for title in titles),
                pK="│".join(str(pukul).center(8, " ") for pukul in pukuls),
                grsD="┬",
                grsPl="┼",
                grsU="┴",
                lok=",".join(str(daerah).ljust(11, " ")
                             for daerah in daerah_sholats)
            )

            table = tables

            # tulis ke file
            with open("/tmp/prayer.tmp", "w") as f:
                f.write(table)

        except:
            pass

        if not os.path.isfile("/tmp/prayer.tmp"):
            write_to_spesicif(loc_default_conky)

        # get_lengh
        with open("/tmp/prayer.tmp", 'r') as f:
            lenght_text = len(f.read())

        if lenght_text > 0:
            write_to_spesicif(loc_update_tmp)
            os.system(
                "cp /tmp/prayer.tmp {home}/.config/conky/prayer_schd/prayer.tmp".format(home=home))

        if lenght_text == 0:
            write_to_spesicif(loc_default_conky)

        # durasi waktu update
        time.sleep(600)


# deg get_lenght():


def write_to_spesicif(location):

    with open("{home}/.config/conky/prayer_schd/conky_schedule.conf".format(home=home), "r") as f:
        read_text = f.readlines()

    write_text = read_text
    write_text[41] = "{location}".format(location=location)

    pj1 = len(write_text)
    with open("{home}/.config/conky/prayer_schd/conky_schedule.conf".format(home=home), "w") as f2:
        for i in range(0, pj1):
            f2.write(write_text[i])


def main():

    url = "https://bimasislam.kemenag.go.id/widget/jadwalshalat/abeaaae01568fdaabedfdceafeabbed89198948c"
    get_source(url)


if __name__ == "__main__":
    main()
