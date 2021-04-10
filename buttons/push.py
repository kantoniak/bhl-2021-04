import RPi.GPIO as GPIO

BUTTON1_PIN = 15
BUTTON2_PIN = 23
BUTTON3_PIN = 25

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def add_buttons_events(button1_callback, button2_callback, button3_callback):
    GPIO.add_event_detect(BUTTON1_PIN, GPIO.RISING, callback=button1_callback, bouncetime=500)
    GPIO.add_event_detect(BUTTON2_PIN, GPIO.RISING, callback=button2_callback, bouncetime=500)
    GPIO.add_event_detect(BUTTON3_PIN, GPIO.RISING, callback=button3_callback, bouncetime=500)


message = input("Press enter to quit\n\n")
