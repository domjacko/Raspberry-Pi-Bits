import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) ## Use Pi Board numbers

pins = [7, 11, 12, 13, 15] ## List of pins
delay = 0.1 ## Time sleep

## Setup each pin to output
for i in range(0, len(pins)):
        print "setup pin" + str(pins[i])
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], False) 

while(True):
        ## LED on
        for i in range(0, len(pins)):
                time.sleep(delay)
                GPIO.output(pins[i], True)
                time.sleep(delay)
                if(i > 0):
                        GPIO.output(pins[i-1], False)
                        GPIO.output(pins[i], False)
                print(i)

        ## LED off
        for i in range(0, len(pins)):
                time.sleep(delay)
                GPIO.output(pins[4-i], True)
                time.sleep(delay)
                if(i > 0):
                        GPIO.output(pins[4-(i-1)],False)
                        GPIO.output(pins[4-i], False)
                print(i)

        print "Off"
GPIO.cleaup()