import board
import RPi.GPIO as GPIO
import time
from display import Display

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

d = Display()

# Count upwards, trigger warning at 20
try:
    d.start()
    v = 0
    while (True):
        v = v + 1
        d.setValue(v)
        if (v == 20):
            d.setWarning(True)
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
except:
    raise
finally:
    d.stop()
