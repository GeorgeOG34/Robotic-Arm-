from __future__ import division
import time
import Adafruit_PCA9685
from Tkinter import *


root = Tk()
root.title('Arm Control')
root.geometry('500x500')

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096  # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#Each of the following variables effectively store the current position that their servo is pointing
#xxxA = Horozontal servo in the shoulder joint (servo 0 on the PCA9685 board)
#xxxB = Vertical servo in the shoulder join (servo 1)
#xxxC = Horozontal servo in the elbow joint (servo 2)
#xxxD = Vertical servo in the elbow join (servo 3)

zzz = 0
half = (servo_max - servo_min) / 2
half = servo_min + half
half = int(half)
#Each servo has 180 degrees of movement, The default position is set to half, meaning from the start each
#servo can move 90 degrees. This also means the arm starts in straight position, at a right angle from whereever the
#'shoulder' is placed
xxxA = half
xxxB = half
xxxC = half
xxxD = half

#This function controls all the arm movement.
#When a button is clicked it calles this function
#There are 8 buttons, 2 for each servos oposite direction
#E.g. servo 0 (xxxA) has a button "left" and "right"
#It gets the amount value, which is the amount of distance it the servo should move by from a text area that the user
#will type in.
def move(serv, amount, direction):
    global xxxA
    global xxxB
    global xxxC
    global xxxD
    global half

    print(str(serv) + ' ' + str(amount))
    zzz = 0
    if serv == 0:
        if direction == 'left':
            goal = xxxA - int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxA - 1 == servo_min:
                    print('min reached')
                    zzz = 1
                elif int(xxxA) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxA = xxxA - 1
                    print(xxxA)
                    pwm.set_pwm(0, 0, xxxA)
                    time.sleep(0.01)

        if direction == 'right':
            goal = xxxA + int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxA + 1 == servo_max:
                    print('min reached')
                    zzz = 1
                elif int(xxxA) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxA = xxxA + 1
                    print(xxxA)
                    pwm.set_pwm(0, 0, xxxA)
                    time.sleep(0.01)
    if serv == 1:
        if direction == 'back':
            goal = xxxB - int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxB - 1 == servo_min:
                    print('min reached')
                    zzz = 1
                elif int(xxxB) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxB = xxxB - 1
                    print(xxxB)
                    pwm.set_pwm(1, 0, xxxB)
                    time.sleep(0.01)

        if direction == 'forward':
            goal = xxxB + int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxB + 1 == servo_max:
                    print('min reached')
                    zzz = 1
                elif int(xxxB) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxB = xxxB + 1
                    print(xxxB)
                    pwm.set_pwm(1, 0, xxxB)
                    time.sleep(0.01)
    if serv == 2:
        if direction == 'left':
            goal = xxxC - int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxC - 1 == servo_min:
                    print('min reached')
                    zzz = 1
                elif int(xxxC) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxC = xxxC - 1
                    print(xxxC)
                    pwm.set_pwm(2, 0, xxxC)
                    time.sleep(0.01)
        if direction == 'right':
            goal = xxxC + int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxC + 1 == servo_max:
                    print('min reached')
                    zzz = 1
                elif int(xxxC) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxC = xxxC + 1
                    print(xxxC)
                    pwm.set_pwm(2, 0, xxxC)
                    time.sleep(0.01)
    if serv == 3:
        if direction == 'back':
            goal = xxxD - int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxD - 1 == servo_min:
                    print('min reached')
                    zzz = 1
                elif int(xxxD) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxD = xxxD - 1
                    print(xxxD)
                    pwm.set_pwm(3, 0, xxxD)
                    time.sleep(0.01)
        if direction == 'forward':
            goal = xxxD + int(amount)
            print('goal ' + str(goal))
            while zzz == 0:
                if xxxD + 1 == servo_max:
                    print('min reached')
                    zzz = 1
                elif int(xxxD) == int(goal):
                    print('done')
                    zzz = 1
                else:
                    xxxD = xxxD + 1
                    print(xxxD)
                    pwm.set_pwm(3, 0, xxxD)
                    time.sleep(0.01)

#This is the gental reset function#
#This is called when the gental reset function is clicked.
#Using time.sleep(0.01) It slowly, returns each servo back to its base position of 90 degrees
def btnRsetCommand():
    global xxxA
    global xxxB
    global xxxC
    global xxxD
    global half
    print('dffff')
    zzz = 0
    if xxxA <= half - 1:
        zzz = 0
        while zzz == 0:
            if xxxA <= half - 1:
                xxxA = xxxA + 1
                pwm.set_pwm(0, 0, xxxA)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxA >= half + 1:
        zzz = 0
        while zzz == 0:
            if xxxA >= half + 1:
                xxxA = xxxA - 1
                pwm.set_pwm(0, 0, xxxA)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxB <= half - 1:
        zzz = 0
        while zzz == 0:
            if xxxB <= half - 1:
                xxxB = xxxB + 1
                pwm.set_pwm(1, 0, xxxB)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxB >= half + 1:
        zzz = 0
        while zzz == 0:
            if xxxB >= half + 1:
                xxxB = xxxB - 1
                pwm.set_pwm(1, 0, xxxB)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxC <= half - 1:
        zzz = 0
        while zzz == 0:
            if xxxC <= half - 1:
                xxxC = xxxC + 1
                pwm.set_pwm(2, 0, xxxC)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxC >= half + 1:
        zzz = 0
        while zzz == 0:
            if xxxC >= half + 1:
                xxxC = xxxC - 1
                pwm.set_pwm(2, 0, xxxC)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxD <= half - 1:
        zzz = 0
        while zzz == 0:
            if xxxD <= half - 1:
                xxxD = xxxD + 1
                pwm.set_pwm(3, 0, xxxD)
                time.sleep(0.01)
            else:
                zzz = 1
    if xxxD >= half + 1:
        zzz = 0
        while zzz == 0:
            if xxxD >= half + 1:
                xxxD = xxxD - 1
                pwm.set_pwm(3, 0, xxxD)
                time.sleep(0.01)
            else:
                zzz = 1

btnRset = Button(root, text='reset', fg='pink', bg='black', command=btnRsetCommand)
btnRset.grid(column=6, row=5)

#This is the hard reset
#All the servos will snap back to there orginal positions fast.
def btnRset2Command():
    print('Hard Reset')
    pwm.set_pwm(0, 0, half)
    pwm.set_pwm(1, 0, half)
    pwm.set_pwm(2, 0, half)
    pwm.set_pwm(3, 0, half)
    pwm.set_pwm(15, 0, half)
btnRset2 = Button(root, text='HARDreset', fg='pink', bg='black', command=btnRset2Command)
btnRset2.grid(column=6, row=6)

#The following functions/buttons are the control buttons for each indicual servo
#Each servo is controlled by two buttons one for each direction
# 1L/1R & 2U/2D are the servos in the shoulder
# 3L/3R & 4U/4D are the servos in the elbow
def btn1LCommand():
    print('motor 1 left')
    add = tb1.get()
    move(0, int(add), 'left')

btn1L = Button(root, text='Left', fg='pink', bg='black', command=btn1LCommand)
btn1L.grid(column=1, row=2)

def btn1RCommand():
    print('motor 1 right')
    add = tb1.get()
    move(0, int(add), 'right')

btn1R = Button(root, text='Right', fg='pink', bg='black', command=btn1RCommand)
btn1R.grid(column=3, row=2)


def btn2UCommand():
    print('motor 2 up')
    add = tb1.get()
    move(1, int(add), 'forward')
btn2U = Button(root, text='Up', fg='pink', bg='black', command=btn2UCommand)
btn2U.grid(column=2, row=1)

def btn2DCommand():
    print('motor 2 down')
    add = tb1.get()
    move(1, int(add), 'back')
btn2D = Button(root, text='Down', fg='pink', bg='black', command=btn2DCommand)
btn2D.grid(column=2, row=4)

def btn3LCommand():
    print('motor 3 left')
    add = tb1.get()
    move(2, int(add), 'left')
btn3L = Button(root, text='Left', fg='pink', bg='black', command=btn3LCommand)
btn3L.grid(column=5, row=2)

def btn3RCommand():
    print('motor 3 right')
    add = tb1.get()
    move(2, int(add), 'right')
btn3R = Button(root, text='Right', fg='pink', bg='black', command=btn3RCommand)
btn3R.grid(column=7, row=2)

def btn4UCommand():
    print('motor 4 up')
    add = tb1.get()
    move(3, int(add), 'forward')
btn4U = Button(root, text='Up', fg='pink', bg='black', command=btn4UCommand)
btn4U.grid(column=6, row=1)

def btn4DCommand():
    print('motor 4 down')
    add = tb1.get()
    move(3, int(add), 'back')
btn4D = Button(root, text='Down', fg='pink', bg='black', command=btn4DCommand)
btn4D.grid(column=6, row=4)

#This is a text area where the user can input how much they want the servo to move by.
tb1 = Entry(root, width=10)
tb1.grid(column=1, row=5)


root.mainloop()







