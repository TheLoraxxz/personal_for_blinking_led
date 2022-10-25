import RPi.GPIO as GPIO
import time


pin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,False)
time.sleep(3)
print("set low")
GPIO.output(pin,True)
print("set high")
time.sleep(10)
GPIO.output(pin,False)
print("set low")
#me.sleep(rand.randint(0,45))
GPIO.cleanup()