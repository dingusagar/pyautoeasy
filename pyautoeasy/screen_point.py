import pyautogui
import time

class ScreenPoint:
    """
    ScreenPoint refers to a point in the screen. All the recorded points are generated here.
    You may use these objects and its methods to quickly create an automation script.
    """

    class Config:
        """Global Configurations for ScreenPoint objects"""
        delay = 1 # each command will be executed after this much delay, unless overidden by the arg ``after_sleeping_for``

    def __init__(self, pos):
        self.pos = pos

    def cursor_here(self, after_sleeping_for=Config.delay):
        """
        move the cursor to this point.
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :return:
        """
        time.sleep(after_sleeping_for)
        pyautogui.moveTo(self.pos[0], self.pos[1])

    def click_here(self, after_sleeping_for=Config.delay, num_of_clicks=1):
        """
        left click on this point.
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :param num_of_clicks: the number of clicks
        :return:
        """
        time.sleep(after_sleeping_for)
        pyautogui.click(x=self.pos[0], y=self.pos[1], clicks=num_of_clicks)

    def double_click_here(self, after_sleeping_for=Config.delay):
        """
        double click on this point.
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :return:
        """
        self.click_here(after_sleeping_for=after_sleeping_for, num_of_clicks=2)

    def triple_click_here(self, after_sleeping_for=Config.delay):
        """
        triple click on this point. useful for selecting the text on the line.
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :return:
        """
        self.click_here(after_sleeping_for=after_sleeping_for, num_of_clicks=3)

    def right_click_here(self, after_sleeping_for=Config.delay):
        """
        right click on this point.
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :return:
        """
        time.sleep(after_sleeping_for)
        pyautogui.click(x=self.pos[0], y=self.pos[1], button='RIGHT')

    def type_here(self, text, enter=True, after_sleeping_for=Config.delay):
        """
        type text using keyboard
        :param text: the text to type
        :param enter: if True, an ENTER key will be pressed after typing the text
        :param after_sleeping_for: sleep for these many seconds before doing the operation.
        :return:
        """
        self.cursor_here(after_sleeping_for=0)
        time.sleep(after_sleeping_for)
        pyautogui.write(text)
        if enter:
            pyautogui.press('enter')