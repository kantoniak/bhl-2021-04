import RPi.GPIO as GPIO
import time

# ABCDEFGABCDEFG...
pins = [
    1, 12, 5, 0, 11, 8, 7, # leftmost digit
    20, 21, 26, 13, 6, 16, 19 # rightmost digit
]

# Maps digit to list of segments, where 0=A, 1=B etc.
digits = [ 
    [1, 2],
    [0, 1, 3, 4, 6],
    [0, 1, 2, 3, 6],
    [1, 2, 5, 6],
    [0, 2, 3, 5, 6],
    [0, 2, 3, 4, 5, 6],
    [0, 1, 2],
    [0, 1, 2, 3, 4, 5, 6]
]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, GPIO.HIGH)

print(pins[3])

# lambda p: pins[p]
def get_pin(p):
    print("PIN: "+str(p)+" -> "+str(pins[p]))
    return pins[p]

while (True):
    for i in range(len(digits)):
        print(digits[i])
        pins = list(map(get_pin, digits[i]))
        print(pins)
        GPIO.output(pins, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(pins, GPIO.HIGH)

GPIO.output(pins, GPIO.LOW)