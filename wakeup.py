# WAKEUP LIGHTS script

import RPi.GPIO as GPIO
import time

duration = 10.0 # 0.5 * 3600.0 # in hours times 3600.0 (float) seconds per hour
steps = 3
stay_on = 5 # 0.5 * 3600 # in hours, time to stay on after full light
min_brightness = 0.1
max_brightness = 100.0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)

p = GPIO.PWM(5, 300) #pin, hertz

p.start(min_brightness)
for(i in range(steps)):
  print (duration / steps)
  p.ChangeDutyCycle(min_brightness + (((max_brightness - min_brightness) / steps) * i))
  time.sleep(duration / steps)
time.sleep(stay_on)
p.stop()
GPIO.cleanup()
