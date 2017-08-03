import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "Setup LED pins as outputs"

GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

GPIO.output(7, True)

time.sleep(2)

GPIO.output(7, False)

raw_input('press enter to exit program')

GPIO.cleanup()

