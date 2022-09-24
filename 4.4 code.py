# ESE519 lab1 part 4.4

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import time
import board
import digitalio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)

apds.enable_proximity = True
apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE
time.sleep(3)
keyboard_layout.write("There is a 'variant' in the matrix. Please try to fix it.\n")
keyboard_layout.write("Use your gesture to control the cursor.\n")
keyboard_layout.write('''
0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0''')

count = 0

while True:
    dist = apds.proximity
    print(dist)

    if dist == 6:
        count = count + 1
        print("count: ", count)
        if count > 20:
            keyboard.send(Keycode.BACKSPACE)
            keyboard.send(Keycode.ZERO)
            break

    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
        keyboard.send(Keycode.UP_ARROW)
        count = 0
    if gesture == 0x02:
        print("down")
        keyboard.send(Keycode.DOWN_ARROW)
        count = 0
    if gesture == 0x03:
        print("left")
        keyboard.send(Keycode.LEFT_ARROW)
        count = 0
    if gesture == 0x04:
        print("right")
        keyboard.send(Keycode.RIGHT_ARROW)
        count = 0


