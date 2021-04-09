import board
import RPi.GPIO as GPIO
import time
from display import *
from FJ8201BH import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DISPLAY_PIN = board.D18
LED_BRIGHTNESS = 0.2

COUNTER_DIGITS = [] # [[ABCDEFG], [ABCDEFG]]
COUNTER_DIGITS.append([20, 21, 26, 13, 6, 16, 19]) # rightmost digit
COUNTER_DIGITS.append([1, 12, 5, 0, 11, 8, 7]) # leftmost digit

d = Display(DISPLAY_PIN, LED_BRIGHTNESS, COUNTER_DIGITS)
v = 0

try:
    d.start()
    d.setValue(v)

    warn = False
    while (True):
        v = v+1
        if (v % 5 == 0):
            d.setWarning(warn)
            warn = not warn
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
except:
    raise
finally:
    d.stop()
