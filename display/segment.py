import RPi.GPIO as GPIO
import time

# ABCDEFGABCDEFG...
pins = [
    1, 12, 5, 0, 11, 8, 7, # leftmost digit
    20, 21, 26, 13, 6, 16, 19 # rightmost digit
]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

while (True):
    for i in range(len(pins)):
        GPIO.output(pins[i], GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(pins[i], GPIO.HIGH)
    break

GPIO.output(pins, GPIO.LOW)