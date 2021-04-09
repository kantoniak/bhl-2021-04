import neopixel
import threading

class Display(object):

    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)

    def __init__(self, pin, brightness):
        self.thread = threading.Thread(target=self.loop)
        self.flag = threading.Event()
        self.shouldStop = False

        self.warning = False
        self.pixels = neopixel.NeoPixel(pin, 1, brightness=brightness)

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
            self.pixels.fill(COLOR_RED)
        else:
            self.pixels.fill(COLOR_GREEN)

    def stop(self):
        self.shouldStop = True
        self.flag.set()
        self.thread.join()
    
    def setWarning(self, value):
        self.warning = value
        self.flag.set()
