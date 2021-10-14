PyAutoEasy
=========

[PyAutoEasy](https://pypi.org/project/pyautoeasy/) is a extension / wrapper around the famous [PyAutoGUI](https://pypi.org/project/PyAutoGUI/), a cross-platform GUI automation tool to replace your boooring repetitive tasks. 

When PyAutoGUI offers powerful ways to control keyboard and mouse movements, PyAutoEasy makes it super easy to grab the cursor positions on the screen and give meaningful names to them and generate the boilerplate program which we can easily modify to suit our needs. 


How to install
============
Thanks to pip! its as simple as :

```
pip install --upgrade pip
pip install pyautoeasy
```


Example Usage
=============

Step 1 : Generate initial code after grabbing the required locations in the screen
--------------------------
1. Open a terminal / command prompt and run 
  ```
  pyautoeasy
  ```
2. Move your cursor to the desired location and press `alt+r` in the keyboard to record the coordinates of a point in the screen.
3. This opens up a dialog box, Now give a name to this point and click OK.
4. Repeat the above 2 steps for all the cursor locations that you want to grab.
5. Press `alt+s` to generate your initial automation script. (`sample.py`)

Step 2 : Modify the generated sample script to suit your needs.
--------------------------
Lets say you wanna create a login automation. Follow step 1 to record all desired locations in the screen like email field, password field, submit button etc.
The generated sample program would look something like this. 
```py
from pyautoeasy import ScreenPoint

email_field = ScreenPoint(pos=(952, 309))
email_field.click_here()

password_field = ScreenPoint(pos=(934, 438))
password_field.click_here()

submit_button = ScreenPoint(pos=(1127, 597))
submit_button.click_here()
```
Now you can take above generated file and easily modify it to something like this. Super easy and intuitive!

```py
from pyautoeasy import ScreenPoint

email_field = ScreenPoint(pos=(952, 309))
email_field.click_here()
email_field.type_here("mytestemail@gmail.com")

password_field = ScreenPoint(pos=(934, 438))
password_field.click_here()
password_field.type_here("password@123")

submit_button = ScreenPoint(pos=(1127, 597))
submit_button.click_here()
```

More about ScreenPoint
=============
* A ScreenPoint object represents a point in your screen with (x,y) cordinates specified in the `pos` argument in the constructor. 

```py
point1 = ScreenPoint(pos=(34, 78))

```

* We can use the ScreenPoint object to move the curser there, click on that point, type something there, right click on that point etc. 
These operations can be done easily by using the following methods :
```py
point1 = ScreenPoint(pos=(34, 78))
point1.click_here() # click on this point
point1.right_click_here() # right click on this point
point1.cursor_here() # move the cursor to this point
point1.type_here("text to type") # type something after selecting this point.
point1.double_click_here() # double click on this point
point1.triple_click_here() # triple click on this point
```

* By default all the operations in ScreenPoint class is done after a delay of `ScreenPoint.Config.delay' (defaults to 1 second).
We can change this property gloabally as follows 

```py
ScreenPoint.Config.delay = 0.5
```

* Alternatively we can even have a delay specified at each operation by passing the argument `after_sleeping_for`.
```py
point1 = ScreenPoint(pos=(34, 78))
point1.click_here(after_sleeping_for=0.5) # click on this point after a delay of 0.5 seconds
point1.right_click_here(after_sleeping_for=0) # right click on this point after a delay of 0 seconds.
```

* type_here() method can take an optional argument `enter=True` which would press an enter key after typing the text. By default `enter=True`

Contribute and Make it better
=============

Any form of contribution is welcome. From finding and reporting bugs to giving feedback to suggesting cool features to building out cool features. Check out [CONTRIBUTING.md](https://github.com/dingusagar/pyautoeasy/blob/main/CONTRIBUTING.md) for more details. 
