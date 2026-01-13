# Simple chaser program created with the Pico 2 W
# With 3 LEDs it blinks them in a sequential fashion
# The duration of each LED is random, to give it a random chaser feel

from machine import Pin
from time import sleep
from random import random, randint, uniform

PGIO_1 = 16
PGIO_2 = 17
PGIO_3 = 18

pg1 = Pin(PGIO_1,Pin.OUT)
pg2 = Pin(PGIO_2,Pin.OUT)
pg3 = Pin(PGIO_3,Pin.OUT)

# Initialize chaser, turn any LEDS off before start
def chaser_init():
    pg1.off()
    pg2.off()
    pg3.off()
    
# Activate LED at specfic Pin
def state(p):
    if p == PGIO_1:
        pg1.on()
        sleep(uniform(0.0,0.5)) # Randomized
        pg1.off()
    elif p == PGIO_2:
        pg2.on()
        sleep(uniform(0.0,0.5)) # Randomized
        pg2.off()
    else:
        pg3.on()
        sleep(uniform(0.0,0.5)) # Randomized
        pg3.off()

# Chaser pattern
def chaser_on(pg_1,pg_2,pg_3):
    while True:
        roll = randint(1,2)
        if roll == 1:
            state(pg_1)
            state(pg_2)
            state(pg_3)
        else:
            state(pg_3)
            state(pg_2)
            state(pg_1)
    
chaser_init()
chaser_on(PGIO_1,PGIO_2,PGIO_3)
