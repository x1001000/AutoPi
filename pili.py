# 1001000.io
import RPi.GPIO as GPIO
import time
import inspect
from bottle import *

Motor_R1_Pin = 16
Motor_R2_Pin = 18
Motor_L1_Pin = 11
Motor_L2_Pin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)

#1/9
def stop():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
#2/9
def forward(seconds):
    #if Motor_R2_Pin or Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#3/9
def turn_R(seconds):
    #if Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#4/9
def turn_L(seconds):
    #if Motor_R2_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#5/9
def backward(seconds):
    #if Motor_R1_Pin or Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#6/9
def back_R(seconds):
    #if Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#7/9
def back_L(seconds):
    #if Motor_R1_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#8/9
def spin_R(seconds):
    #if Motor_R1_Pin or Motor_L2_Pin: stop()
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]
#9/9
def spin_L(seconds):
    #if Motor_R2_Pin or Motor_L1_Pin: stop()
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(seconds)
    stop()
    return inspect.stack()[0][3]

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def javascripts(filename):
    return static_file(filename, root='static/css')

@route('/')
def index():
    output = template('view')
    return output



keep_time = 0.5
turn_time = 0.25
spin_time = 2
moving = 'forward'
count = 0
@route('/ajax', method='POST')
def ajax():
    global keep_time
    global turn_time
    global spin_time
    global moving
    global count

    arrow = request.forms.get("arrow")

    stop_key = (87, 83, 65, 68)

    if int(arrow) == 119:
        moving = forward(keep_time)

    if int(arrow) == 115:
        moving = backward(keep_time)

    if int(arrow) == 100:
        if moving in ['forward', 'turn_R', 'turn_L']:
            if moving == 'turn_R':
                count += 1
            else:
                count = 0
            moving = turn_R(turn_time)
            if count > 5:
                spin_R(spin_time)
                count = 0
        if moving in ['backward', 'back_R', 'back_L']:
            if moving == 'back_R':
                count += 1
            else:
                count = 0
            moving = back_R(turn_time)
            if count > 5:
                spin_L(spin_time)
                count = 0

    if int(arrow) == 97:
        if moving in ['forward', 'turn_R', 'turn_L']:
            if moving == 'turn_L':
                count += 1
            else:
                count = 0
            moving = turn_L(turn_time)
            if count > 5:
                spin_L(spin_time)
                count = 0
        if moving in ['backward', 'back_R', 'back_L']:
            if moving == 'back_L':
                count += 1
            else:
                count = 0
            moving = back_L(turn_time)
            if count > 5:
                spin_R(spin_time)
                count = 0

    if int(arrow) in stop_key:
        stop()

try:
    run(host='0.0.0.0', port=80)

finally:
    stop()
    GPIO.cleanup()