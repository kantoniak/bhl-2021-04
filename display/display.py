from enum import Enum
import neopixel
import time
import threading
from FJ8201BH import *

class BlinkState(Enum):
    not_blinking = 0
    visible = 1
    hidden = 2

class Display(object):

    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)
    NO_COLOR = (0, 0, 0)

    BLINK_VISIBLE_TIME = 0.8
    BLINK_HIDDEN_TIME = 0.5

    def __init__(self, pin, ledBrightness, counterDigits):
        self.thread = threading.Thread(target=self.loop)
        self.flag = threading.Event()
        self.shouldStop = False

        self.value = 0
        self.counterDisplay = FJ8201BH(counterDigits)

        self.pixels = neopixel.NeoPixel(pin, 1, brightness=ledBrightness)

        self.warning = False
        self.blinkState = BlinkState.not_blinking
        self.lastBlinkChange = time.time()

    def start(self):
        self.counterDisplay.start()
        self.flag.clear()
        self.thread.start()

    def loop(self):
        while (not self.shouldStop):

            if (self.blinkState == BlinkState.hidden):
                self.counterDisplay.setValue(None)
            else:
                self.counterDisplay.setValue(self.value)

            if (self.warning == True):
                self._updateBlink()
            else:
                self.pixels.fill(self.COLOR_GREEN)
                self.flag.wait()

        self.counterDisplay.stop()
        self.pixels.deinit()

    def stop(self):
        self.shouldStop = True
        self.flag.set()
        self.thread.join()

    def setWarning(self, value):
        if (self.warning == value):
            return

        self.warning = value
        if (self.warning):
            self._startBlinking()
        else:
            self._stopBlinking()
        self.flag.set()

    def setValue(self, value):
        self.value = value
        self.flag.set()

    def _startBlinking(self):
        self.pixels.fill(self.COLOR_RED)
        self.blinkState = BlinkState.visible
        self.lastBlinkChange = time.time()

    def _stopBlinking(self):
        self.blinkState = BlinkState.not_blinking
        self.lastBlinkChange = None

    def _updateBlink(self):
        current_time = time.time()
        last_time = self.lastBlinkChange
        delta = current_time - last_time
        if (self.blinkState == BlinkState.visible):
            if (delta > self.BLINK_VISIBLE_TIME):
                self.pixels.fill(self.NO_COLOR)
                self.blinkState = BlinkState.hidden
                self.lastBlinkChange = current_time
            self.flag.wait(self.BLINK_VISIBLE_TIME - delta)
        elif (self.blinkState == BlinkState.hidden):
            if (delta > self.BLINK_HIDDEN_TIME):
                self.pixels.fill(self.COLOR_RED)
                self.blinkState = BlinkState.visible
                self.lastBlinkChange = current_time
            self.flag.wait(self.BLINK_HIDDEN_TIME - delta)
        else:
            self.flag.wait()

