import RPi.GPIO as GPIO
import time ## Needed for sleep function

GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.OUT) ## Set Pins to OUTput
GPIO.setup(17, GPIO.OUT)

## Main function of program which loops round LEDs
def Go(numTimes):
        currentTurn = 4 
        for i in range(0, numTimes):
                print "Iteration: " + str(i+1)
                ## Checks which LED should blink next
                ## and sends pin number to Blink function
                if(currentTurn == 4): 
                        Blink(4)
                        currentTurn = 17
                if(currentTurn == 17):
                        Blink(17)
                        currentTurn = 4 
        print "Done!"
        GPIO.cleanup()
        
## Function to make the LEDs flash
def Blink(pin):
        print str(pin) + "'s turn"
        GPIO.output(pin, True) ## Turn LED on
        time.sleep(0.1) ## Pause
        GPIO.output(pin, False) ## Turn LED off
        time.sleep(0.1) ## Pause again

Go(15)
