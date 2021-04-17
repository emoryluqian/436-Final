from bluetooth import *
import sys

from connection import connect_port

import time
import numpy as np
import matplotlib.pyplot as plt

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
sock = connect_port()
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#right
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#left
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#up
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#down
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#enter
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True:
    data = []
    time.sleep(0.1)
    if GPIO.input(10) == GPIO.HIGH:
        data.append(" left")
    if GPIO.input(10) == GPIO.HIGH:
        data.append(" right")
    if GPIO.input(10) == GPIO.HIGH:
        data.append(" up")
    if GPIO.input(10) == GPIO.HIGH:
        data.append(" down")
    if GPIO.input(10) == GPIO.HIGH:
        data.append(" enter")
    sock.send(data)
sock.close()