# WAKEUP LIGHTS script

import RPi.GPIO as GPIO
import time
import os
import math

duration = 30 * 60.0 # in minutes times 60.0 (float) seconds per hour
stay_on = 15 * 60 # in minutes, time to stay on after full light

os.system("gpio -g mode 18 pwm")

for i in range(1025):
   print i
   os.system("gpio -g pwm 18 %d" % i)
   time.sleep(duration / 1024.0)
time.sleep(stay_on)
os.system("gpio -g pwm 18 0")
