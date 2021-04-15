# Script to move the camera slider motor
# Goal is to have two buttons, one to move left the other to move right
# The speed and length of the movement will be hardcoded in the script

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from gpiozero import Button
from time import sleep,time
import signal
import sys

# Change these values only!
MOVEMENT_CM = 70
SPEED = 8


# Speed mapping
# The higher the number, the slower the speed!
SPEED_MAPPING = {
    1: "Full",
    2: "Half",
    4: "1/4",
    8: "1/8",
    16: "1/16",
    32: "1/32"
}


#define GPIO pins
direction= 20 # direction pin
step = 21 # step pin
EN_pin = 24 # enable pin
MX_pins = (14,15,18) # M0-2

 
# Steps per revolution, multipltied by the step division (basically results in the speed)
SPR = 200 * SPEED
# 1 full turn ~4cm
MOVEMENT_REVOLUTION = 3.98

# Create motor instance, with the M0-2 pins
slider_motor = RpiMotorLib.A4988Nema(direction, step, MX_pins, "DRV8825")

GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

def move(movement_direction):
    # Wait a second before starting the movment
    sleep(0.5)

    GPIO.output(EN_pin,GPIO.LOW) # Set enable to low, to enable motor

    slider_motor.motor_go(movement_direction, # True=Clockwise, False=Counter-Clockwise
                        SPEED_MAPPING[SPEED] , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                        int(abs(SPR / MOVEMENT_REVOLUTION * MOVEMENT_CM)),
                        .0005, # step delay [sec]
                        False, # True = print verbose output
                        .05) # initial delay [sec]

    GPIO.output(EN_pin,GPIO.HIGH) # disable motor

def left(btn):
    start_time = round(time() * 1000)
    MOVEMENT_DIRECTION = True
    print("left button pressed")

    move(True)

    print("movement finished duration: {}".format(round(time() * 1000) - start_time))

def right(btn):
    start_time = round(time() * 1000)
    MOVEMENT_DIRECTION = False
    print("right button pressed")

    move(False)

    print("movement finished duration: {}".format(round(time() * 1000) - start_time))

button1 = Button(2)
button2 = Button(3)

button1.when_pressed = left
button2.when_pressed = right

signal.pause()
