import RPi.GPIO as GPIO

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
        print(allPins)
        GPIO.setup(allPins, GPIO.OUT)
        GPIO.output(allPins, GPIO.HIGH)

    def stop(self):
        allPins = self._flatten(self.digitsToPins)
        GPIO.output(allPins, GPIO.HIGH)

    def setValue(self, value):
        if (value == None or value < 0):
            toDisplay = [None, None]
        else:
            toDisplay = [value % 10, (value // 10) % 10]
            if toDisplay[1] == 0:
                toDisplay[1] = None

        self._setDigit(0, toDisplay[0])
        self._setDigit(1, toDisplay[1])

    def _setDigit(self, numFromRight, value):
        if (self.display[numFromRight] == value):
            return

        segmentsToPins = self.digitsToPins[numFromRight]
        allDigitPins = list(map(lambda s: segmentsToPins[s], self.ALL_SEGMENTS))
        if (value == None):
            GPIO.output(allDigitPins, GPIO.HIGH)
            self.display[numFromRight] = None
            return

        # Light up active
        segments = self.DIGIT_TO_SEGMENTS[value]
        pins = list(map(lambda s: segmentsToPins[s], segments))
        GPIO.output(pins, GPIO.LOW)

        # Turn down others
        nonPins = [x for x in allDigitPins if x not in pins]
        GPIO.output(nonPins, GPIO.HIGH)

        self.display[numFromRight] = value

    def _flatten(self, l):
        return [item for sublist in l for item in sublist]
