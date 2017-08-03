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
pwm = GPIO.PWM(PWM_PIN, 50)
pwm.start(7.5)

try:
    while True:
        # Duty Change
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        # Duty Change
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        # Duty Change
        pwm.ChangeDutyCycle(2.5)
        time.sleep(3)

except KeyboardInterrput:
    pwm.stop()
    GPIO.cleanup()