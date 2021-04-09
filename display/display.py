import time
import board
import neopixel
import threading

color_green = (0, 255, 0)
color_red = (255, 0, 0)

class Display(object):

    def __init__(self):
        self.warning = False
        self.shouldStop = False
        self.pixels = neopixel.NeoPixel(board.D18, 1, brightness=0.5)
        self.thread = threading.Thread(target=self.loop)

    def start(self):
        self.thread.start()

    def loop(self):
        while (not self.shouldStop):
            self.pixels.fill(color_green)
            time.sleep(1)
            self.pixels.fill(color_red)
            time.sleep(1)
        self.pixels.deinit()
    
    def stop(self):
        self.shouldStop = True
        self.thread.join()


d = Display()
try:
    d.start()
    while (True):
        pass
except KeyboardInterrupt:
    pass
finally:
    d.stop()
