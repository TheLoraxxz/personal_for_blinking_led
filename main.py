import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,False)
print("set low")
GPIO.output(15,True)
print("set high")
time.sleep(10)
GPIO.output(15,False)
print("set low")
#me.sleep(rand.randint(0,45))
GPIO.cleanup()