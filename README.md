# Raspberry Pi Motion Detector

An array of connected motion detectors which play sounds when triggered.

The idea behind this project was to get a handful of lower power infrared motion sensors and set them up around the house let the kids run wild. When a motion sensor is triggered we simply play the mp3 assigned to the sensor. I've put the sensors inside empty paper towel rolls to narrow the motion area.

## Sensors
I am currently using 2 Low Voltage PIR Infrared Motion Sensor Detect Module (STK01-14002216). They aren't terrible the only issue I have with them is when triggered they stay HI for around 30 seconds. I would prefer a shorter or adjustable timing.

## Software
Raspbian linux, python, GPIO, and mpg123 to play the sounds.

    sudo apt-get install mpg123
    sudo apt-get install python-dev
    sudo apt-get install python-rpi.gpio

## Run

    sudo ./motion.py
