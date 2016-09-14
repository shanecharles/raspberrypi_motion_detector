#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

# setup the motion sensor dictionary 
# the pin as the key and (Bool, mp3 to play)
sensors = dict([(18, (False,"1.mp3")),
                (23, (False, "2.mp3"))])

for pin, _ in sensors.items():
    GPIO.setup(pin, GPIO.IN)

def check_sensor(pin, (old_state, music)):
    motion = GPIO.input(pin)
    if motion and not old_state:
        print "movement on motion: " + str(pin)
        subprocess.Popen(["mpg123",music])
    elif not motion and old_state:
        print "movement stopped: " + str(pin)

    return (motion, music)

while True:
    for pin, state in sensors.items():
        sensors[pin] = check_sensor(pin, state)
        
    sleep(0.1)
