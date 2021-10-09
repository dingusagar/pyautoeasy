import pyautogui
import time

class ScreenPoint:
    class Config:
        delay = 1
    def __init__(self, pos):
        self.pos = pos

    def cursor_here(self, after_sleeping_for=Config.delay):
        time.sleep(after_sleeping_for)
        pyautogui.moveTo(self.pos[0], self.pos[1])

    def click_here(self, after_sleeping_for=Config.delay):
        time.sleep(after_sleeping_for)
        pyautogui.click(x=self.pos[0], y=self.pos[1])

    def right_click_here(self, after_sleeping_for=Config.delay):
        time.sleep(after_sleeping_for)
        pyautogui.click(x=self.pos[0], y=self.pos[1], button='RIGHT')

    def type_here(self, text, enter=True, after_sleeping_for=Config.delay):
        self.cursor_here(after_sleeping_for=0)
        time.sleep(after_sleeping_for)
        pyautogui.write(text)
        if enter:
            pyautogui.press('enter')