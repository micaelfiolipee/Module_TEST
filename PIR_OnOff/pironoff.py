import RPi.GPIO as GPIO
import time

PIR = 8

LED = 7

pirState = False                        # we start, assuming no motion detected
pirVal = False                          # we start, assuming no motion detected

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
    pirVal = GPIO.input(PIR)            # read input value
    if (pirVal == True):                # check if the input is HIGH
        GPIO.output(LED, True)          # turn LED ON
        if (pirState == False):
            # we have just turned on
            pirState = True
    else:
        GPIO.output(LED, False)         # turn LED OFF
        if (pirState == True):
            # we have just turned off
            time.sleep(2)
            pirState = False;
