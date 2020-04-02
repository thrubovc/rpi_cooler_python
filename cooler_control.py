#!/usr/bin/env python3

from time import sleep
import os
import RPi.GPIO as GPIO

pin = 18
maxTemp = 65
minTemp = 45
flagPrevious = 'OFF'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)


def getCPUtemperature():
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    temp = (res.replace("temp=", "").replace("'C\n", ""))
    return temp


def writeFile(state):
    f = open('/home/pi/cooler/fan_state', 'w')
    f.write("Current CPU temperature: " + str(getCPUtemperature()) + "'C\n")
    f.write('The fan is ' + state + '\n')
    f.close()


def setPin(mode):
    GPIO.output(pin, mode)
    return()


def fanON():
    setPin(True)
    writeFile('ON')
    return()


def fanOFF():
    setPin(False)
    writeFile('OFF')
    return()


def setFlag():
    cpuTemp = float(getCPUtemperature())
    if cpuTemp > maxTemp:
        flag = 'ON'
        return(flag)
    elif cpuTemp < minTemp:
        flag = 'OFF'
        return(flag)
    else:
        if flagPrevious == 'OFF':
            flag = 'OFF'
            return(flag)
        else:
            flag = 'ON'
            return(flag)
    return(flag)


def execute():
    flag = str(setFlag())
    if os.path.exists('/home/pi/cooler/on'):
        fanON()
    else:
        if flag == 'ON':
            fanON()
        else:
            fanOFF()
        global flagPrevious
        flagPrevious = flag
        return(flagPrevious)


while True:
    execute()
    sleep(5)
