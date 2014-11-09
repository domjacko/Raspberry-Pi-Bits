## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Bluetooth Searcher for searching for nearby 
## bluetooth devices using the device name, LEDs
## will flash dependant on if the device is found
## written by domjacko
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import bluetooth
import RPi.GPIO as GPIO
import time

## Bluetooth setup
target_name = "Nexus 4"
target_address = None


## GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

print "Searching for devices..."
nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
	if target_name == bluetooth.lookup_name(bdaddr):
		target_address = bdaddr
		break

if target_address is not None:
	print "Found target bluetooth device with address ", target_address
	GPIO.output(15, True)
	time.sleep(3)
	GPIO.output(15, False)
else:
	print "Could not find target bluetooth device nearby"
	GPIO.output(7, True)
	time.sleep(3)
	GPIO.output(7, False)
GPIO.cleanup()
