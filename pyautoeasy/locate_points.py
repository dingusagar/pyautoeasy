import json
from queue import Queue

import pyautogui
from pynput import keyboard

MODIFIER_KEYS = {
    'ctrl': 'Key.ctrl',
    'alt': 'Key.alt',
    'cmd': 'Key.cmd',
}

message_queue = Queue()
QUEUE_POLLING_INTERVAL = 0.5

class InteractivePositionLocator:
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
        position_variable_name = pyautogui.prompt(f'Recording position ({x},{y}). Variable name :')
        if position_variable_name:
            self.saved_cursor_positions[position_variable_name] = (x, y)
        print(f'Recording Cursor Position at ({x},{y}) as variable {position_variable_name}')

    def on_press(self, key):
        key = str(key).strip("'")
        self.pressed_keys.add(key)
        print("Key pressed: {0}".format(key))

        if self.KEY_COMBINATION_SAVE.issubset(self.pressed_keys):
            message_queue.put(None)
        elif self.KEY_COMBINATION_RECORD_CURSOR.issubset(self.pressed_keys):
            message_queue.put(key)
        print(self.pressed_keys)

    def on_release(self, key):
        key = str(key).strip("'")
        print("Key released: {0}".format(key))
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)
        print(self.pressed_keys)

    def generate_program(self):
        sample_program_file_name = self.output_file
        print(f'Generating sample program : {sample_program_file_name}')

        program_lines = ['from pyautoeasy import ScreenPoint', '\n']

        for variable_name, pos in self.saved_cursor_positions.items():
            program_lines.append(f'{variable_name} = ScreenPoint(pos={pos})')
            program_lines.append(f'{variable_name}.click_here()')
            program_lines.append('\n')

        program = '\n'.join(program_lines)
        print(program)
        with open(sample_program_file_name, 'w') as file:
            file.write(program)

    def grab_cursor_positions(self):
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

        while True:
            print('polling queue..')
            data = message_queue.get()
            print(f'Data : {data}')
            if not data:
                print('Stopping Keyboard listeners..')
                listener.stop()
                break
            self.record_cursor_pos()

        print(f'Saving cursor positions : {self.saved_cursor_positions}...')
        with open('saved_cursor_positions.json', 'w') as convert_file:
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
