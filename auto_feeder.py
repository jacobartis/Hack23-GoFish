from datetime import datetime as dt
from time import sleep as sl
from ast import literal_eval as lit_eval
from Servo import feeding_time

times = []

def update_times():
    time_file = open("auto_feed_times.txt")
    for time in time_file.readlines():
        times.append(lit_eval(time.strip()))

def start_check():
    update_times()
    while True:
        if times.__contains__([dt.now().hour,dt.now().minute,dt.now().second]):
            feeding_time(5)
        sl(1)

