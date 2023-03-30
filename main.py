import psutil
import datetime
import os
import time


while True:
    f = open('digital_health.txt', 'r')
    should_time = f.readline(6)
    f.close()
    now_time = datetime.datetime.today()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    up_time = now_time-boot_time
    up_time_2 = str(up_time).split('.')[0]
    up_time_h = up_time_2.split(':')[0]
    up_time_min = up_time_2.split(':')[1]
    up_time_sec = up_time_2.split(':')[2]
    up_time_3 = up_time_h+up_time_min+up_time_sec
    f = open('digital_health.txt', 'w')
    f.write(should_time)
    f.write(str(up_time).split('.')[0])
    f.close()
    if int(up_time_3) >= int(should_time):
        os.system('notify-send Digital-Health "Deine Bildschirmzeit für heute vorbei" --icon=/home/luca/Luca/Privat/Python/digitalhealth/Lazarus_GUI/digital_health.ico')
        break
    time.sleep(1)
