import RPi.GPIO as GPIO
import time
import requests

#Moves the servo back and forth 10 times
def feeding_time(freq):
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    try:
        for x in range(freq):
            print(x)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

def flashbang():
    url = 'http://localhost:5000/flashbang'
    x = requests.get(url)
    return(x)
