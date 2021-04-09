from display import Display
import time

DISPLAY_PIN = 18
LED_BRIGHTNESS = 0.5

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
finally:
    d.stop()
