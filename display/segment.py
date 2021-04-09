import RPi.GPIO as GPIO

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW)