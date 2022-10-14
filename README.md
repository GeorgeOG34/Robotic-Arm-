# Robotic-Arm-
This was built using a raspberry pi, 4 servos (2x 7kg & 2x 35kg), a PCA9685 and a 3D printer

arm.py is the GUI controls, which will run on the raspberry pi.
The arm works by having two "joints" a shoulder and an elbow. For the program to work with no editing, ensure the following servos are connected to the correct positions on the PCA9685:

The horizontal shoulder servo - position 0
The vertical shoulder servo - position 1
The horizontal elbow servo - position 2
The vertical elbow servo - postion 3.

Using the program:
There are 8 buttons, 4 for each joint, 2 for each servo. 
The buttons on the GUI are layed out like two lots of WASD.
Simply, input a number into the text area and click a button, and that servo will move.

Here you can see my robotic arm working. I'm using a custom physical controller in this video to control it as opposed to the GUI controller in this repository, but its still the same arm: https://imgur.com/a/mAmrH7h
