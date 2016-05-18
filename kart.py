# 1001000.io
import RPi.GPIO as GPIO
import time
import readchar

Motor_R1_Pin = 16
Motor_R2_Pin = 18
Motor_L1_Pin = 11
Motor_L2_Pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)

#move1/9
def stop():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
#move2/9
def forward():
    #if Motor_R2_Pin or Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
#move3/9
def forward_R():
    #if Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
#move4/9
def forward_L():
    #if Motor_R2_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
#move5/9
def backward():
    #if Motor_R1_Pin or Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
#move6/9
def backward_R():
    #if Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
#move7/9
def backward_L():
    #if Motor_R1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
#move8/9
def clockwise():
    #if Motor_R1_Pin or Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
#move9/9
def counterclockwise():
    #if Motor_R2_Pin or Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)

U = '\x1b[A'
D = '\x1b[B'
R = '\x1b[C'
L = '\x1b[D'

pause = 0.4
delay = 0.5

while True:
    t1 = time.time()
    key = readchar.readkey()
    t2 = time.time()
    continued = True if t2-t1 < pause else False

    if key == U:
        forward()
        motion = 'forward'

    if key == D:
        backward()
        motion = 'backward'

    if key == R:
        if continued:
            if motion == 'forward':
                forward_R()
            elif motion == 'backward':
                backward_R()
            else:
                clockwise()
        else:
            clockwise()
            motion = 'clockwise'

    if key == L:
        if continued:
            if motion == 'forward':
                forward_L()
            elif motion == 'backward':
                backward_L()
            else:
                counterclockwise()
        else:
            counterclockwise()
            motion = 'counterclockwise'

    if key == ' ':
        break
    time.sleep(delay)
    stop()

GPIO.cleanup()
