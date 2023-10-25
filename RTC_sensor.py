import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIN_SENSOR = 17
GPIO.setup(PIN_SENSOR, GPIO.IN)

def read_sensor():
		return GPIO.input(PIN_SENSOR)

try:
	while True:
		if read_sensor():
				print("température élevée")
		else:
				print("")
		time.sleep(1)
except KeyboardInterrupt:
	print("programme interrompu")
finally:
	GPIO.cleanup()
