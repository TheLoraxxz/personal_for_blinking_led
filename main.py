import RPi.GPIO as GPIO
import random as rand
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.LOW)
rand.seed(102758)
GPIO.output(15,GPIO.HIGH)
time.sleep(3)
GPIO.output(15,GPIO.LOW)
#me.sleep(rand.randint(0,45))