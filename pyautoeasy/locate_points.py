import json

import pyautogui
import pymsgbox
from pynput.keyboard import Listener as KeyboardListener

KEY_COMBINATION_SAVE = {'Key.alt', 's'}
KEY_COMBINATION_RECORD_CURSOR = {'Key.alt', 'r'}

# The currently active modifiers
pressed_keys = set()
saved_cursor_positions = {}


def stop_listeners():
    print('stopping all listeners..')
    keyboard_listener.stop()


def record_cursor_pos():
    x, y = pyautogui.position()
    position_variable_name = pymsgbox.prompt(f'Recording position ({x},{y}). Variable name :')
    if position_variable_name:
        saved_cursor_positions[position_variable_name] = (x, y)
    print(f'Recording Cursor Position at ({x},{y}) as variable {position_variable_name}')


def on_press(key):
    global pressed_keys
    key = str(key).strip("'")
    pressed_keys.add(key)
    print("Key pressed: {0}".format(key))

    if KEY_COMBINATION_SAVE.issubset(pressed_keys):
        stop_listeners()
    elif KEY_COMBINATION_RECORD_CURSOR.issubset(pressed_keys):
        record_cursor_pos()
    print(pressed_keys)


def on_release(key):
    global pressed_keys
    key = str(key).strip("'")
    print("Key released: {0}".format(key))
    if key in pressed_keys:
        pressed_keys.remove(key)
    print(pressed_keys)


keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
keyboard_listener.start()
keyboard_listener.join()

print(f'Saving cursor positions : {saved_cursor_positions}...')

with open('../saved_cursor_positions.json', 'w') as convert_file:
    convert_file.write(json.dumps(saved_cursor_positions))

sample_program_file_name = '../generated_program.py'
print(f'Generating sample program : {sample_program_file_name}')

program_lines = ['from pyautoeasy import ScreenPoint', '\n']

for variable_name, pos in saved_cursor_positions.items():
    program_lines.append(f'{variable_name} = ScreenPoint(pos={pos})')
    program_lines.append(f'{variable_name}.click_here()')
    program_lines.append('\n')

program = '\n'.join(program_lines)
print(program)
with open(sample_program_file_name, 'w') as file:
    file.write(program)
