# Including Library
import RPi.GPIO as GPIO
import time

# Define Using PinNo and Other Variables
PWM_PIN = 18

# Initializing GPIO Port
GPIO.setmode(GPIO.BCM)
# Initializing Pins
GPIO.setup(PWM_PIN, GPIO.OUT)
# Initializing Pin for PWM
pwm = GPIO.PWM(PWM_PIN,50)

pwm.start(12.5)
time.sleep(0.5)
pwm.stop()
pwm.start(7.5)
time.sleep(0.5)
pwm.stop
pwm.start(10.0)
time.sleep(0.5)
pwm.stop()

# Custom Variables
var = 1

try:
    while True:
        # Wait Key Press
        var = raw_input("Enter L / R / C: ")

        # if 'R' Pressed
        if var == 'R':
            print 'R'
            # RUN PWM PIN
            pwm.start(2.5)
            time.sleep(1)
            pwm.stop()
        # if 'L' Pressed
        elif var == 'L':
            print 'L'
            # RUN PWM PIN
            pwm.start(12.5)
            time.sleep(1)
            pwm.stop()
        # if 'C' Pressed
        elif var == 'C':
            print 'C'
            # RUN PWM PIN
            pwm.start(7.5)
            time.sleep(1)
            pwm.stop()

except KeyboardInterrput:
    pwm.stop()
    GPIO.cleanup()
