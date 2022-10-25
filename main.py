import RPi.GPIO as GPIO
import time


pin = 29
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,False)
print("set low")
GPIO.output(pin,True)
print("set high")
time.sleep(10)
GPIO.output(pin,False)
print("set low")
#me.sleep(rand.randint(0,45))
GPIO.cleanup()