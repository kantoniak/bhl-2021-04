import RPi.GPIO as GPIO
import time

# [ABCDEFG, ABCDEFG]
pinsInUse = []
pinsInUse.append([20, 21, 26, 13, 6, 16, 19]) # rightmost digit
pinsInUse.append([1, 12, 5, 0, 11, 8, 7]) # leftmost digit

class FJ8201BH(object):

    # Maps digit to list of segments, where 0=A, 1=B etc.
    DIGIT_TO_SEGMENTS = [
        [0, 1, 2, 3, 4, 5],
        [1, 2],
        [0, 1, 3, 4, 6],
        [0, 1, 2, 3, 6],
        [1, 2, 5, 6],
        [0, 2, 3, 5, 6],
        [0, 2, 3, 4, 5, 6],
        [0, 1, 2],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]
    ]

    ALL_SEGMENTS = [0, 1, 2, 3, 4, 5, 6]

    def __init__(self, digitsToPins):
        self.digitsToPins = digitsToPins
        self.display = [None, None] # Right to left

    def start(self):
        allPins = self._flatten(self.digitsToPins)
        GPIO.setup(allPins, GPIO.OUT)
        GPIO.output(allPins, GPIO.HIGH)

    def stop(self):
        allPins = self._flatten(self.digitsToPins)
        GPIO.output(allPins, GPIO.HIGH)

    def _setDigit(self, numFromRight, value):
        if (self.display[numFromRight] == value):
            return

        if (value == None):
            GPIO.output(self.ALL_SEGMENTS, GPIO.HIGH)
            self.display[numFromRight] = None
            return

        segments = self.DIGIT_TO_SEGMENTS[value]
        segmentsToPins = self.digitsToPins[numFromRight]
        pins = list(map(lambda s: segmentsToPins[s], segments))
        GPIO.output(pins, GPIO.LOW)
        nonPins = [x for x in self.ALL_SEGMENTS if x not in pins]
        GPIO.output(nonPins, GPIO.HIGH)

        self.display[numFromRight] = value

    def _flatten(self, l):
        return [item for sublist in l for item in sublist]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

c = FJ8201BH(pinsInUse)
toDisplay = [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c.start()
while (True):
    for i in range(len(toDisplay)):
        c._setDigit(1, toDisplay[i])

c.stop()