import RPi.GPIO as GPIO
import time

phase0 = 23
phase1 = 22
phase2 = 27
phase3 = 17

delay = 0.1
FinalDelay = 0.025
StepRamp = 0.0001

repeat = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(phase0, GPIO.OUT)
GPIO.setup(phase1, GPIO.OUT)
GPIO.setup(phase2, GPIO.OUT)
GPIO.setup(phase3, GPIO.OUT)


try:
    while repeat > 0:
        GPIO.output(phase0, 1)
        GPIO.output(phase1, 0)
        GPIO.output(phase2, 0)
        GPIO.output(phase3, 0)
        time.sleep(delay)
        GPIO.output(phase0, 0)
        GPIO.output(phase1, 1)
        GPIO.output(phase2, 0)
        GPIO.output(phase3, 0)
        time.sleep(delay)
        GPIO.output(phase0, 0)
        GPIO.output(phase1, 0)
        GPIO.output(phase2, 1)
        GPIO.output(phase3, 0)
        time.sleep(delay)
        GPIO.output(phase0, 0)
        GPIO.output(phase1, 0)
        GPIO.output(phase2, 0)
        GPIO.output(phase3, 1)
        time.sleep(delay)
        if delay > FinalDelay:
            delay = delay - StepRamp
        repeat = repeat - 1

except KeyboardInterrupt:
        GPIO.output(phase0, 0)
        GPIO.output(phase1, 0)
        GPIO.output(phase2, 0)
        GPIO.output(phase3, 0)
        GPIO.cleanup()
        print "KeyboardInterrupt"
        raise

except:
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  

finally:  
    GPIO.cleanup()  # this ensures a clean exit

