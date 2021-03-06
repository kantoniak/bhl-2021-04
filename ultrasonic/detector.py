from sound_sensor import UltrasoundSensor
import RPi.GPIO as GPIO
import time

GPIO_TRIGGER_ENTER = 18
GPIO_ECHO_ENTER = 15
GPIO_TRIGGER_EXIT = 24
GPIO_ECHO_EXIT = 23

# GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':

    try:
        sensor = UltrasoundSensor(GPIO_TRIGGER_ENTER, GPIO_ECHO_ENTER, GPIO_TRIGGER_EXIT, GPIO_ECHO_EXIT)

        sensor.start()
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        sensor.stop()
        print("Stopped.")
        GPIO.cleanup()

