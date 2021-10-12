import json
from queue import Queue

import pyautogui
from pynput import keyboard
import os

DOC_STRING_FOR_GENERATED_PROGRAM = '''
\"\"\"
_________________________________________________________________________________________
ScreenPoint refers to a point in the screen. All the recorded points are generated here.
You may use these objects and its methods to quickly create an automation script.
_________________________________________________________________________________________
\"\"\"
'''

MODIFIER_KEYS_LINUX = {
    'ctrl': 'Key.ctrl',
    'alt': 'Key.alt',
    'cmd': 'Key.cmd',
}


MODIFIER_KEYS_WINDOWS = {
    'ctrl': 'Key.ctrl_l',
    'alt': 'Key.alt_l',
}
if os.name == 'nt': #windows machine
    MODIFIER_KEYS = MODIFIER_KEYS_WINDOWS
else:
    MODIFIER_KEYS = MODIFIER_KEYS_LINUX

message_queue = Queue()
QUEUE_POLLING_INTERVAL = 0.5

class InteractivePositionLocator:
    """
    Interactive tool to grab the x,y positions of desired locations in the screen.
    Assign variable names to these positions and generate a sample.py program.
    """
    KEY_COMBINATION_SAVE = {'Key.alt', 's'}
    KEY_COMBINATION_RECORD_CURSOR = {'Key.alt', 'r'}

    def __init__(self, output_file, save_key='alt+s', cursor_record_key='alt+r'):
        self.saved_cursor_positions = {}

        # The currently active modifiers
        self.pressed_keys = set()
        self.output_file = output_file if output_file.endswith('.py') else output_file + '.py'

        self.KEY_COMBINATION_SAVE = self.get_keys(save_key)
        self.KEY_COMBINATION_RECORD_CURSOR = self.get_keys(cursor_record_key)
        self.stop_listener = False

    def record_cursor_pos(self):
        x, y = pyautogui.position()
        position_variable_name = pyautogui.prompt(
            f'Recording cursor position ({x},{y}).\n Give a name to refer to this position:')
        if position_variable_name:
            self.saved_cursor_positions[position_variable_name] = (x, y)
            print(f'\nRecording Cursor Position at ({x},{y}) as variable {position_variable_name}')

    def on_press(self, key):
        key = str(key).strip("'")
        self.pressed_keys.add(key)
        if self.KEY_COMBINATION_SAVE.issubset(self.pressed_keys):
            message_queue.put(None)
        elif self.KEY_COMBINATION_RECORD_CURSOR.issubset(self.pressed_keys):
            message_queue.put(key)

    def on_release(self, key):
        key = str(key).strip("'")
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def generate_program(self):
        sample_program_file_name = self.output_file
        print(f'\nGenerating sample automation program : {sample_program_file_name}')

        program_lines = []
        program_lines.append(DOC_STRING_FOR_GENERATED_PROGRAM)
        program_lines.append('from pyautoeasy import ScreenPoint\n')
        for variable_name, pos in self.saved_cursor_positions.items():
            program_lines.append(f'{variable_name} = ScreenPoint(pos={pos})')
            program_lines.append(f'{variable_name}.click_here()')
            program_lines.append('\n')

        program = '\n'.join(program_lines)
        with open(sample_program_file_name, 'w') as file:
            file.write(program)

    def grab_cursor_positions(self):
        """
        Start interactive program to grab the cursor positions.
        :return:
        """
        keyboard_listeners = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        keyboard_listeners.start()

        while True:
            data = message_queue.get()
            if not data:
                print('Stopping Keyboard and mouse listeners..')
                keyboard_listeners.stop()
                break
            self.record_cursor_pos()

        print(f'Saving the following cursor positions : {self.saved_cursor_positions} to cursor_positions.json')
        with open('cursor_positions.json', 'w') as convert_file:
            convert_file.write(json.dumps(self.saved_cursor_positions))

        self.generate_program()

    def get_keys(self, key_combination):
        keys = set()
        key_combination = key_combination.strip().split('+')
        for key in key_combination:
            if key in MODIFIER_KEYS:
                keys.add(MODIFIER_KEYS[key])
            else:
                keys.add(key)
        return keys


if __name__ == '__main__':
    locator = InteractivePositionLocator(output_file='sample', save_key='alt+s', cursor_record_key='alt+r')
    locator.grab_cursor_positions()
