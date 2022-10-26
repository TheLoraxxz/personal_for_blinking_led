import RPi.GPIO as GPIO
import time
import random

#setup
pin = 8
random.seed("iris haloween party")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,False)
while True:
    time.sleep(random.randint(12,20))
    GPIO.output(pin,True)
    time.sleep(0.3)
    GPIO.output(pin,False)