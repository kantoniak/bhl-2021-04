import board
from display import Display
import time

DISPLAY_PIN = board.D18
LED_BRIGHTNESS = 0.2

d = Display(DISPLAY_PIN, LED_BRIGHTNESS)
try:
    d.start()

    warn = False
    while (True):
        d.setWarning(warn)
        warn = not warn
        time.sleep(1)
except KeyboardInterrupt:
    pass
except:
    raise
finally:
    d.stop()
