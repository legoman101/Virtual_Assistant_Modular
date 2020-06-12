# CamJam EduKit 3 - Robotics
# Wii controller remote control script

import time # Import the Time library
import os
import cwiid
from pynput.keyboard import Key, Controller

keyboard = Controller()

def key(text):
    keyboard.press(text)
    keyboard.release(text)

def shiftkey(text):
    with keyboard.pressed(Key.shift):
        keyboard.press(text)
        keyboard.release(text)

def word(text):
    keyboard.type(text)

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    wii=cwiid.Wiimote()

except RuntimeError:
    print "Error opening wiimote connection"
    # Uncomment this line to shutdown the Pi if pairing fails
    #os.system("sudo halt")
    quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN

while True:

    buttons = wii.state['buttons']

    # If Plus and Minus buttons pressed
    # together then rumble and quit.
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
        print '\nClosing connection ...'
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        os.system("sudo halt")
        exit(wii)
  
    # Check if other buttons are pressed by
    # doing a bitwise AND of the buttons number
    # and the predefined constant for that button.
    if(buttons & cwiid.BTN_A):
        print 'A Pressed'
        word('//takecommand')
        key(Key.enter)
        time.sleep(0.2)