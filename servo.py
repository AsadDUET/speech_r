# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
# from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import random

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 375  # Max pulse length out of 4096
servo_mid = int((servo_min+servo_max)/2)
side_left=300
side_right=150
side_mid=int((side_left+side_right)/2)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
print('press Ctrl-C to quit...')

def up():
    pwm.set_pwm(0, 0, servo_max)
    pwm.set_pwm(1, 0, servo_min)
    pwm.set_pwm(2, 0, side_mid)
def slow_up():
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_mid+i)
        pwm.set_pwm(1, 0, servo_mid-i)
        pwm.set_pwm(2, 0, side_mid)
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_max-i)
        pwm.set_pwm(1, 0, servo_min+i)
        pwm.set_pwm(2, 0, side_mid)
def down():
    pwm.set_pwm(0, 0, servo_min)
    pwm.set_pwm(1, 0, servo_max)
    pwm.set_pwm(2, 0, side_mid)
def mid():
    pwm.set_pwm(0, 0, servo_mid)
    pwm.set_pwm(1, 0, servo_mid)
    pwm.set_pwm(2, 0, side_mid)
def left_tilt():
    pwm.set_pwm(0, 0, servo_max)
    pwm.set_pwm(1, 0, servo_max)
    pwm.set_pwm(2, 0, side_mid)
def slow_left_tilt():
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_mid+i)
        pwm.set_pwm(1, 0, servo_mid+i)
        pwm.set_pwm(2, 0, side_mid)
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_max-i)
        pwm.set_pwm(1, 0, servo_max-i)
        pwm.set_pwm(2, 0, side_mid)
def right_tilt():
    pwm.set_pwm(0, 0, servo_min)
    pwm.set_pwm(1, 0, servo_min)
    pwm.set_pwm(2, 0, side_mid)
def slow_right_tilt():
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_mid-i)
        pwm.set_pwm(1, 0, servo_mid-i)
        pwm.set_pwm(2, 0, side_mid)
    for i in range(0,servo_max-servo_mid):
        time.sleep(.01)
        pwm.set_pwm(0, 0, servo_min+i)
        pwm.set_pwm(1, 0, servo_min+i)
        pwm.set_pwm(2, 0, side_mid)
def talking():
    mid()
    time.sleep(.1)
    pwm.set_pwm(0, 0, servo_mid-random.randint(-2,2)*15)
    time.sleep(.1)
    pwm.set_pwm(1, 0, servo_mid-random.randint(-2,2)*15)
    time.sleep(.1)
    pwm.set_pwm(2, 0, side_mid)
    time.sleep(.1)
    mid()
def left_turn():
    pwm.set_pwm(0, 0, servo_mid)
    pwm.set_pwm(1, 0, servo_mid)
    pwm.set_pwm(2, 0, side_left)
def right_turn():
    pwm.set_pwm(0, 0, servo_mid)
    pwm.set_pwm(1, 0, servo_mid)
    pwm.set_pwm(2, 0, side_right)

def listening_led():
    pwm.set_pwm(14, 0, 4000)
    pwm.set_pwm(15, 0, 0)
def processing_led():
    pwm.set_pwm(14, 0, 0)
    pwm.set_pwm(15, 0, 4000)
def listen_end():
    down()
    time.sleep(.3)
    mid()
    time.sleep(.3)
def motion():
    down()
    time.sleep(.5)
    up()
    time.sleep(.5)
    left_tilt()
    time.sleep(.5)
    right_tilt()
    time.sleep(.5)
    mid()
    time.sleep(.5)
def slow_motion():
    j=random.randint(0,2)
    if j is 0:
        slow_up()
    if j is 1:
        slow_left_tilt()
    if j is 2:
        slow_right_tilt()

if __name__=="__main__":
    mid()
