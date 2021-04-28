from bluetooth import *
import sys

from connection import connect_port

import time
import numpy as np

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
sock = connect_port()
# GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#right
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#left
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#up
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#down
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#enter
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True:
    data = ""
    time.sleep(0.1)
    if not GPIO.input(16):
        data += " left"
    if not GPIO.input(17):
        data += " right"
    if not GPIO.input(27):
        data += " up"
    if not GPIO.input(22):
        data += " down"
    if not GPIO.input(23):
        data += " enter"
    # arr = (map(lambda e: bytes(e,"utf-8"), data))
    print(data)
    sock.send(data)
sock.close()