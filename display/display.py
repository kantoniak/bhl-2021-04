import neopixel
import threading
from FJ8201BH import *

class Display(object):

    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)

    def __init__(self, pin, ledBrightness, counterDigits):
        self.thread = threading.Thread(target=self.loop)
        self.flag = threading.Event()
        self.shouldStop = False

        self.value = 0
        self.counterDisplay = FJ8201BH(counterDigits)

        self.warning = False
        self.pixels = neopixel.NeoPixel(pin, 1, brightness=ledBrightness)

    def start(self):
        self.counterDisplay.start()
        self.flag.clear()
        self.thread.start()

    def loop(self):
        while (not self.shouldStop):
            self._update()
            self.flag.wait()
        self.counterDisplay.stop()
        self.pixels.deinit()
    
    def _update(self):
        self.counterDisplay.setValue(self.value)
        if (self.warning):
            self.pixels.fill(self.COLOR_RED)
        else:
            self.pixels.fill(self.COLOR_GREEN)

    def stop(self):
        self.shouldStop = True
        self.flag.set()
        self.thread.join()
    
    def setWarning(self, value):
        self.warning = value
        self.flag.set()
    
    def setValue(self, value):
        self.value = value
        self.flag.set()
