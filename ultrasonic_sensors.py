import RPi.GPIO as GPIO
import time
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
print("start")

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(GPIO_TRIGGER, True)
        
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        
        StartTime = time.time()
        StopTime = time.time()
        
        while GPIO.input(GPIO_ECHO)==0:
            StartTime = time.time()
            
        while GPIO.input(GPIO_ECHO)==1:
            StopTime = time.time()
            
        
        TimeElapsed = StopTime - StartTime
        
        distance = round((TimeElapsed * 34300)/2, 2)
        temperature = sensor.get_temperature()
        print("Distance=", distance)
        print("Temp: %s celsius" %temperature)
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
