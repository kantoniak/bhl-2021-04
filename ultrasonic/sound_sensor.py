import threading
from ultra_sensor import distance
import RPi.GPIO as GPIO
import time
import math

class UltrasoundSensor(object):

    MIN_LEN = 0.4
    INIT_TIME = 2
    TIMEOUT = 2

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
        self.initSensor()

        sequence = ""
        interval_start = math.inf

        while (self.run):
            enter_dist = distance(self.TRIGER_ENTER, self.ECHO_ENTER)
            exit_dist = distance(self.TRIGER_EXIT, self.ECHO_EXIT)

            # print("Enter: %.1f cm" % enter_dist)
            # print("Exit: %.1f cm" % exit_dist)

            enter_state = self.enterLen * self.MIN_LEN > enter_dist
            exit_state = self.exitLen * self.MIN_LEN > exit_dist

            if (enter_state and (not sequence or (sequence and sequence[0] != '1'))):
                sequence += "1"
                if(len(sequence) == 1):
                    interval_start = time.time()

            elif (exit_state and (not sequence or (sequence and sequence[0] != '2'))):
                sequence += "2"
                if(len(sequence) == 1):
                    interval_start = time.time()
            
            if (sequence == "12"):
                self.counter += 1
                print("Enter detected.")
                sequence = ""
                time.sleep(0.2)

            elif (sequence == "21"):
                self.counter -= 1
                print("Exit detected.")
                sequence = ""
                time.sleep(0.2)

            
            if (len(sequence) > 2 or sequence == "11" or sequence == "22" or time.time() - interval_start > self.TIMEOUT):
                sequence = ""
                interval_start = math.inf

            # print("\n\n")
            time.sleep(0.1)
        print("Ultrasound sensor loop ended.")

    def initSensor(self):
        start_time = time.time()
        
        enterSum = 0
        exitSum = 0
        n = 0
        while (time.time() - start_time < self.INIT_TIME):
            enterSum += distance(self.TRIGER_ENTER, self.ECHO_ENTER)
            exitSum += distance(self.TRIGER_EXIT, self.ECHO_EXIT)
            n += 1
            time.sleep(0.1)
        self.enterLen = enterSum / n
        self.exitLen = exitSum / n

        print("Enter sensor length: %.1f cm" % self.enterLen)
        print("Exit sensor length: %.1f cm" % self.exitLen)

