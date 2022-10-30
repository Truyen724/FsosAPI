#sudo apt-get install python-rpi.gpio python3-rpi.gpio
import RPi.GPIO as GPIO
from time import sleep 

PORT_GPIO = 11

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT_GPIO, GPIO.OUT, initial=GPIO.LOW) 
while True:
 GPIO.output(PORT_GPIO, GPIO.HIGH)
 sleep(0.5) 
 GPIO.output(PORT_GPIO, GPIO.LOW) 
 sleep(0.5) 