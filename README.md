PyAutoEasy
=========

PyAutoEasy is a utility wrapper around the famous [PyAutoGUI](https://pypi.org/project/PyAutoGUI/), a cross-platform GUI automation Python module. 

When PyAutoGUI offers powerful ways to control keyboard and mouse movements, PyAutoEasy makes it super easy to grab the cursor positions on the screen and give meaningful names to them and generate the boilerplate program which we can easily modify to suit our needs. 


How to install
============

`pip install pyautoeasy`


Example Usage
=============

Step 1 : Generate initial code after grabbing the required locations in the screen
--------------------------
1. Open a terminal / command prompt and run `pyautoeasy`
2. Move your cursor to the desired location and press `alt+r` in the keyboard to record a location point.
3. This opens up a dialog box, Now give a name to this cursor location in the box.
4. Repeat the above 2 steps for all the cursor locations that you want to grab.
5. Press `alt+s` to generate your initial automation script. (`sample.py`)

Step 2 : Modify the sample script to suit your needs.
--------------------------
1. Open a terminal / command prompt and run `pyautoeasy`
2. Move your cursor to the desired location and press `alt+r` in the keyboard to record a location point.
3. This opens up a dialog box, Now give a name to this cursor location in the box.
4. Repeat the above 2 steps for all the cursor locations that you want to grab.
5. Press `alt+s` to generate your initial automation script. (`sample.py`)
6. Easily make necessary changes on the script using the ScreenPoint methods present in this module. 


The x, y coordinates used by PyAutoGUI has the 0, 0 origin coordinates in the top left corner of the screen. The x coordinates increase going to the right (just as in mathematics) but the y coordinates increase going down (the opposite of mathematics). On a screen that is 1920 x 1080 pixels in size, coordinates 0, 0 are for the top left while 1919, 1079 is for the bottom right.

Currently, PyAutoGUI only works on the primary monitor. PyAutoGUI isn't reliable for the screen of a second monitor (the mouse functions may or may not work on multi-monitor setups depending on your operating system and version).

All keyboard presses done by PyAutoGUI are sent to the window that currently has focus, as if you had pressed the physical keyboard key.

```python
    >>> import pyautogui
    >>> screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    >>> currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    >>> pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    >>> pyautogui.click() # Click the mouse at its current location.
    >>> pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    >>> pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    >>> pyautogui.doubleClick() # Double click the mouse at the
    >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
    >>> pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    >>> pyautogui.press('esc') # Simulate pressing the Escape key.
    >>> pyautogui.keyDown('shift')
    >>> pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
    >>> pyautogui.keyUp('shift')
    >>> pyautogui.hotkey('ctrl', 'c')
```

Display Message Boxes
---------------------
```python
    >>> import pyautogui
    >>> pyautogui.alert('This is an alert box.')
    'OK'
    >>> pyautogui.confirm('Shall I proceed?')
    'Cancel'
    >>> pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
    'B'
    >>> pyautogui.prompt('What is your name?')
    'Al'
    >>> pyautogui.password('Enter password (text will be hidden)')
    'swordfish'
```

Screenshot Functions
--------------------

(PyAutoGUI uses Pillow for image-related features.)
```python
    >>> import pyautogui
    >>> im1 = pyautogui.screenshot()
    >>> im1.save('my_screenshot.png')
    >>> im2 = pyautogui.screenshot('my_screenshot2.png')
```
You can also locate where an image is on the screen:
```python
    >>> import pyautogui
    >>> button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    >>> button7location
    (1416, 562, 50, 41)
    >>> buttonx, buttony = pyautogui.center(button7location)
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
```
The locateCenterOnScreen() function returns the center of this match region:
```python
    >>> import pyautogui
    >>> buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
```

How Does PyAutoGUI Work?
========================

The three major operating systems (Windows, macOS, and Linux) each have different ways to programmatically control the mouse and keyboard. This can often involve confusing, obscure, and deeply technical details. The job of PyAutoGUI is to hide all of this complexity behind a simple API.

* On Windows, PyAutoGUI accesses the Windows API (also called the WinAPI or win32 API) through the built-in `ctypes` module. The `nicewin` module at https://github.com/asweigart/nicewin provides a demonstration for how Windows API calls can be made through Python.

* On macOS, PyAutoGUI uses the `rubicon-objc` module to access the Cocoa API.

* On Linux, PyAutoGUI uses the `Xlib` module to access the X11 or X Window System.


Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
