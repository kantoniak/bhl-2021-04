import threading
from ultra_sensor import distance
import RPi.GPIO as GPIO
import time

class UltrasoundSensor(object):

    MIN_LEN = 0.5
    INIT_TIME = 2
    TIME_SPAN = 2

    def __init__(self, triger_enter,  echo_enter, triger_exit, echo_exit):
        self.TRIGER_ENTER = triger_enter
        self.ECHO_ENTER = echo_enter
        self.TRIGER_EXIT = triger_exit
        self.ECHO_EXIT = echo_exit

        self.run = False
        self.thread = threading.Thread(target=self.loop)
        self.flag = threading.Event()

        self.counter = 0
        self.enterLen = 0
        self.exitLen = 0

    def start(self):
        GPIO.setup(self.TRIGER_ENTER, GPIO.OUT)
        GPIO.setup(self.ECHO_ENTER, GPIO.IN)
        GPIO.setup(self.TRIGER_EXIT, GPIO.OUT)
        GPIO.setup(self.ECHO_EXIT, GPIO.IN)

        self.run = True
        self.flag.clear()
        self.thread.start()

    def stop(self):
        self.run = False
        self.flag.set()
        self.thread.join()

    def getCounter(self):
        tmp = self.counter
        self.counter = 0
        return tmp

    def loop(self):
        start_time = time.time()
        
        enterSum = 0
        exitSum = 0
        n = 0
        while (time.time() - start_time < self.INIT_TIME):
            enterSum += distance(self.TRIGER_ENTER, self.ECHO_ENTER)
            exitSum += distance(self.TRIGER_EXIT, self.ECHO_EXIT)
            n += 1
        self.enterLen = enterSum / n
        self.exitLen = exitSum / n

        print("Enter sensor length: %.1f cm" % self.enterLen)
        print("Exit sensor length: %.1f cm" % self.exitLen)

        last_time = time.time()
        enter_crossed = False
        exit_crossed = False

        while (self.run):
            enter_dist = distance(self.TRIGER_ENTER, self.ECHO_ENTER)
            exit_dist = distance(self.TRIGER_EXIT, self.ECHO_EXIT)

            print("Enter: %.1f cm" % enter_dist)
            print("Exit: %.1f cm" % exit_dist)

            enter_state = self.enterLen * self.MIN_LEN >= enter_dist
            exit_state = self.exitLen * self.MIN_LEN >= exit_dist

            
            if (enter_crossed and not exit_crossed):
                if (exit_state):
                    print("Enter detected.")
                    self.counter += 1
                    enter_crossed = True
                    exit_crossed = True
                    continue

            elif (not enter_crossed and exit_crossed):
                if (enter_state):
                    print("Exit detected.")
                    self.counter -= 1
                    enter_crossed = True
                    exit_crossed = True
                    continue

            enter_crossed = enter_state
            exit_crossed = exit_state
            print("\n\n")
            time.sleep(1)

        print("Ultrasound sensor loop ended.")