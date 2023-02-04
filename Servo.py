import RPi.GPIO as GPIO
from playwright.sync_api import Playwright, sync_playwright
import time

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

def flash_bang():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()

        page.goto("http://10.2.177.147:8080/")

        button = page.query_selector("#flashbtn")
        button.click()

        browser.close()