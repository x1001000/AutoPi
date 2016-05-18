# 1001000.io
import RPi.GPIO as GPIO
import time

Motor_R1_Pin = 16
Motor_R2_Pin = 18
Motor_L1_Pin = 11
Motor_L2_Pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)
TRIG = 40
ECHO = 37
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def stop():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
def forward(t):
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
def forward_R(t):
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
def forward_L(t):
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)

def distance():
    GPIO.output(TRIG, False)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
      pulse_start = time.time()
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    #distance = round(distance, 2)
    #time.sleep(0.06)
    return distance

delay = 0.4
turn  = 0.2

try:
  while True:
    before = distance()
    forward()
    time.sleep(delay)
    stop()
    after = distance()
    diff = after - before
    #print before,after
    if after > 10 and diff > 0:
      forward_R()
      time.sleep(turn)
      stop()
    elif after < 5 and diff < 0:
      forward_L()
      time.sleep(turn)
      stop()
    else:
      continue

except:
  GPIO.cleanup()
