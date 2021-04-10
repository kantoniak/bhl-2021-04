import RPi.GPIO as GPIO
import time
   
def distance(triger, echo):
    GPIO.output(triger, True)
 
    time.sleep(0.00001)
    GPIO.output(triger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(echo) == 0:
        StartTime = time.time()
 
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 