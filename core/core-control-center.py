import os
import sys
sys.path.append(os.getcwd() + '/../client')

import client

import board
import RPi.GPIO as GPIO
import time
from display.display import Display

from buttons.push import add_buttons_events


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DISPLAY_SLEEP = 0.2
CONVEY_LIMIT = 5
UPDATE_API_CYCLES_COUNT = 50


def get_api_data():
    return int(client.get_stats()['current'])


display = Display()
counter = get_api_data()


def reset_callback(channel):
    print("Button 'RESET was pushed!")
    global counter
    counter = 0
    display.setValue(counter)
    client.reset()


def enter_callback(channel):
    print("Button '+1' was pushed!")
    global counter
    counter += 1
    display.setValue(counter)
    client.entered()


def exit_callback(channel):
    print("Button '-1' was pushed!")
    global counter
    counter -= 1
    display.setValue(counter)
    client.exited()


if __name__ == "__main__":
    add_buttons_events(reset_callback, enter_callback, exit_callback)

    cycles = 0
    try:
        display.start()
        while True:
            display.setValue(counter)
            display.setWarning(counter >= CONVEY_LIMIT)

            cycles += 1
            cycles %= UPDATE_API_CYCLES_COUNT

            if cycles == 0:
                global counter
                counter = get_api_data()

            time.sleep(DISPLAY_SLEEP)
    except KeyboardInterrupt:
        pass
    except:
        raise
    finally:
        display.stop()
        GPIO.cleanup()
