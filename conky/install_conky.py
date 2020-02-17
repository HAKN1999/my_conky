#!/usr/bin/python

from os.path import expanduser
import os
import subprocess
import time

home = expanduser("~")

# cek apakah dir .config/autostart sudah ada
if not os.path.isdir("{home}/.config/autostart".format(home=home)):
    # belum ada buat dir
    print "Membuat folder {home}/.config/autostart".format(home=home)
    os.mkdir("{home}/.config/autostart".format(home=home))

# cek apakah dir .config/conky sudah ada
if not os.path.isdir("{home}/.config/conky".format(home=home)):
    print "\nMembuat folder {home}/.config/conky".format(home=home)
    os.mkdir("{home}/.config/conky".format(home=home))

# cek apakah dir .fonts sudah ada
# if not os.path.isdir("{home}/.fonts".format(home=home)):
#     print "\nMembuat folder {home}/.fonts".format(home=home)
#     os.mkdir("{home}/.fonts".format(home=home))

# hapus file jika ada di dalam folder .config/conky untuk
# menghindari crash saat installasi
# ? harus nya proses ini untuk melihat ada file di dalam conky atau tidak,
# jika tidak masuk ke opsi else,tapi tetap menjalankan opsi if user_pilih
cek = subprocess.check_output(
    ["ls -a",  "{home}/.config/conky".format(home=home)], shell=True)
if len(cek) > 0:
    user_pilih = raw_input(
        "Semua di dalam folder conky akan di hapus untuk menghindari crash installasi,(y/n): ")
    if user_pilih == 'y' or 'Y':
        # os.system("rm -r {home}/.config/conky/*".format(home = home))
        time.sleep(1)
        print "\nInstallasi folder sudah kosong,file akan di copy"
    else:
        print("\nTidak ada perubahan di file conky,installasi berhenti!")
        exit()
else:
    pass

# copy file download ke .config/conky
print "\nFile akan di copy ke ~/.config/conky"
os.system("cp -r * {home}/.config/conky".format(home=home))
time.sleep(1)

# membuat file autostart untuk otomatis aktif saat booting
print "\nMembuat file autostart , untuk booting selanjutnya"
os.system(
    "cp %s/.config/conky/start_conky.desktop %s/.config/autostart/start_conky.desktop" % (home, home))
os.system(
    "cp %s/.config/conky/weather/weather.desktop %s/.config/autostart/weather.desktop" % (home, home))

# ! bug copy mode root
# installasi font
# print "Installasi fonts"
# user_root = os.getenv("SUDO_USER")
# if user_root is None:
#     print "Program ini membutuhkan hak root dengan 'sudo'"
#     exit()
# os.system("sudo apt install conky-all && sudo apt install vnstat")
# os.system("cp fonts/* /usr/share/fonts")

print "\nInstallasi selesai"
print "\nUntuk melihat perubahan tampilan restart system"
