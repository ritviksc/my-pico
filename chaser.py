# Simple chaser program created with the Pico 2 W
# With 3 LEDs it blinks them in a sequential fashion
# The duration of each LED is random, to give it a random chaser feel

from machine import Pin
from time import sleep
from random import random, uniform

# Initialize chaser, turn any LEDS off before start
def chaser_init(pg1,pg2,pg3):
    Pin(pg1,Pin.OUT).off()
    Pin(pg2,Pin.OUT).off()
    Pin(pg3,Pin.OUT).off()
    
# Activate LED at specfic Pin
def state(p):
    Pin(p,Pin.OUT).on()
    sleep(uniform(0.0,0.5)) # Randomized
    Pin(p,Pin.OUT).off()

# Chaser pattern
def chaser_on(pg1,pg2,pg3):
    while True:
        state(pg1)
        state(pg2)
        state(pg3)
    
chaser_init(16,17,18)
chaser_on()
