from datetime import datetime as dt
from time import sleep as sl
from ast import literal_eval as lit_eval
from Servo import feeding_time

times = []

#Updates the times list with times in the auto feed list
def update_times():
    times.clear()
    time_file = open("auto_feed_times.txt")
    file_times = time_file.readlines()
    
    if len(file_times) == 1:
        times.append(lit_eval(file_times.strip()))
    else:
        for time in file_times:
            if time != "\n":
                times.append(lit_eval(time.strip()))

#Checks the current time against the list of set times every second
def start_check():
    while True:
        update_times()
        if times.__contains__([dt.now().hour,dt.now().minute,dt.now().second]):
            feeding_time(5)
        sl(1)
        

