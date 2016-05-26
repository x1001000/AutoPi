import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG1 = 36
TRIG2 = 38
TRIG3 = 40

ECHO1 = 22
ECHO2 = 24
ECHO3 = 26

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)

GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(ECHO3,GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
GPIO.output(TRIG3, False)

try:
  while True:
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)
    while GPIO.input(ECHO1)==0:
      pulse_start1 = time.time()
      #print 1
    while GPIO.input(ECHO1)==1:
      pulse_end1 = time.time()
      #print 2
    pulse_duration1 = pulse_end1 - pulse_start1
    distance1 = pulse_duration1*17150
    distance1 = round(distance1, 1)
    print distance1
    time.sleep(0.06)

    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)
    while GPIO.input(ECHO2)==0:
      pulse_start2 = time.time()
      #print 3
    while GPIO.input(ECHO2)==1:
      pulse_end2 = time.time()
      #print 4
    pulse_duration2 = pulse_end2 - pulse_start2
    distance2 = pulse_duration2*17150
    distance2 = round(distance2, 1)
    print distance1,distance2
    time.sleep(0.06)

    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)
    while GPIO.input(ECHO3)==0:
      pulse_start3 = time.time()
      #print 5
    while GPIO.input(ECHO3)==1:
      pulse_end3 = time.time()
      #print 6
    pulse_duration3 = pulse_end3 - pulse_start3
    distance3 = pulse_duration3*17150
    distance3 = round(distance3, 1)
    print distance1,distance2,distance3
    time.sleep(0.06)

except:
  GPIO.cleanup()
