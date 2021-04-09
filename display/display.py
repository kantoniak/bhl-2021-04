import time
import board
import neopixel
import threading

color_green = (0, 255, 0)
color_red = (255, 0, 0)

class Display(object):

    def __init__(self):
        self.thread = threading.Thread(target=self.loop)
        self.flag = Event()
        self.shouldStop = False

        self.warning = False
        self.pixels = neopixel.NeoPixel(board.D18, 1, brightness=0.5)

    def start(self):
        self.flag.clear()
        self.thread.start()

    def loop(self):
        while (not self.shouldStop):
            self.update()
            self.flag.wait()
        self.pixels.deinit()
    
    def update(self):
        if (self.warning):
            self.pixels.fill(color_red)
        else:
            self.pixels.fill(color_green)

    def stop(self):
        self.shouldStop = True
        self.flag.set()
        self.thread.join()
    
    def setWarning(self, value):
        self.warning = value
        self.flag.set()


d = Display()
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
