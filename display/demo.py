import board
import RPi.GPIO as GPIO
import time
from display import *
from FJ8201BH import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DISPLAY_PIN = board.D18
LED_BRIGHTNESS = 1

COUNTER_DIGITS = [] # [[ABCDEFG], [ABCDEFG]]
COUNTER_DIGITS.append([20, 21, 26, 13, 6, 16, 19]) # rightmost digit
COUNTER_DIGITS.append([1, 12, 5, 0, 11, 8, 7]) # leftmost digit

d = Display(DISPLAY_PIN, LED_BRIGHTNESS, COUNTER_DIGITS)

try:
    d.start()
    d.setValue(58)
    d.setWarning(True)

    while (True):
        pass
except KeyboardInterrupt:
    pass
except:
    raise
finally:
    d.stop()
