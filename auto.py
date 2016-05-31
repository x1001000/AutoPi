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
TRIG = [36, 38, 40]
ECHO = [22, 24, 26]
for N in TRIG:
    GPIO.setup(N, GPIO.OUT, initial=GPIO.LOW)
for N in ECHO:
    GPIO.setup(N, GPIO.IN)
time.sleep(2)

def stop():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(0.01)
def forward(t):
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()
def turnRight(t):
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()
def turnLeft(t):
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()
def spinRight(t):
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()
def spinLeft(t):
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(t)
    stop()
def distance(N):
    GPIO.output(TRIG[N], True)
    time.sleep(0.00001)
    GPIO.output(TRIG[N], False)
    while GPIO.input(ECHO[N])==0:
      pulse_start = time.time()
    while GPIO.input(ECHO[N])==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    #distance = round(distance, 2)
    #time.sleep(0.06)
    return distance

interval = 0.06
L,F,R = range(3)

try:
    while True:
        while distance(F) < 20:
            spinLeft(interval)
        before = distance(R)
        forward(interval)
        after = distance(R)
        diff = after - before
        if after < 8:
            turnLeft(interval)
        if diff < 0:
            turnLeft(interval)
        else:
            turnRight(interval)
        if before > 60 and after > 60:
            forward(interval*5)
            spinRight(interval*5)
            forward(interval*5)
except:
    print 'except'
    GPIO.cleanup()
