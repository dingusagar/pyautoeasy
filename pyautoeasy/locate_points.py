import json

import pyautogui
from pynput import keyboard
import os
from pyautoeasy.screenshot_utils import take_screenshot
from pyautoeasy.shared_queue import send_message, receive_message, MESSAGE_TYPE
from pyautoeasy.point_metadata import CursorPointMetaData, ImageMetaData

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
if os.name == 'nt':  # windows machine
    MODIFIER_KEYS = MODIFIER_KEYS_WINDOWS
else:
    MODIFIER_KEYS = MODIFIER_KEYS_LINUX


class InteractivePositionLocator:
    """
    Interactive tool to grab the x,y positions of desired locations in the screen.
    Assign variable names to these positions and generate a sample.py program.
    """
    KEY_COMBINATION_SAVE = {'Key.alt', 's'}
    KEY_COMBINATION_RECORD_CURSOR = {'Key.alt', 'r'}
    KEY_COMBINATION_GRAB_IMAGE = {'Key.alt', 'f'}

    def __init__(self, output_file, save_key='alt+s', cursor_record_key='alt+r', image_capture_key='alt+f'):
        # self.saved_cursor_positions = {}
        self.meta_info_list = []

        # The currently active modifiers
        self.pressed_keys = set()
        self.output_file = output_file if output_file.endswith('.py') else output_file + '.py'

        self.KEY_COMBINATION_SAVE = self.get_keys(save_key)
        self.KEY_COMBINATION_RECORD_CURSOR = self.get_keys(cursor_record_key)
        self.KEY_COMBINATION_GRAB_IMAGE = self.get_keys(image_capture_key)
        self.stop_listener = False

    def record_cursor_pos(self):
        x, y = pyautogui.position()
        position_variable_name = pyautogui.prompt(
            f'Recording cursor position ({x},{y}).\n Give a name to refer to this position:')
        if position_variable_name:
            point_meta_data = CursorPointMetaData(x_cord=x, y_cord=y, variable_name=position_variable_name)
            self.meta_info_list.append(point_meta_data)
            print(f'\nRecording Cursor Position at ({x},{y}) as variable {position_variable_name}')

    def on_press(self, key):
        key = str(key).strip("'")
        self.pressed_keys.add(key)
        if self.KEY_COMBINATION_SAVE.issubset(self.pressed_keys):
            send_message(MESSAGE_TYPE.SAVE_AND_EXIT)
        elif self.KEY_COMBINATION_RECORD_CURSOR.issubset(self.pressed_keys):
            send_message(MESSAGE_TYPE.RECORD_POSITION)
        elif self.KEY_COMBINATION_GRAB_IMAGE.issubset(self.pressed_keys):
            send_message(MESSAGE_TYPE.GRAB_IMAGE)

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

        for metadata in self.meta_info_list:
            if type(metadata) == CursorPointMetaData:
                pos = (metadata.x_cord, metadata.y_cord)
                program_lines.append(f'{metadata.variable_name} = ScreenPoint(pos={pos})')
                program_lines.append(f'{metadata.variable_name}.click_here()')
                program_lines.append('\n')

            elif type(metadata) == ImageMetaData:
                program_lines.append(
                    f'{metadata.variable_name} = ScreenPoint.from_image(image_path={metadata.image_path})')
                program_lines.append(f'{metadata.variable_name}.click_here()')
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
            command, data = receive_message()
            if command == MESSAGE_TYPE.SAVE_AND_EXIT:
                print('Stopping Keyboard and mouse listeners..')
                keyboard_listeners.stop()
                break
            elif command == MESSAGE_TYPE.RECORD_POSITION:
                self.record_cursor_pos()
            elif command == MESSAGE_TYPE.GRAB_IMAGE:
                take_screenshot()
            elif command == MESSAGE_TYPE.CAPTURED_IMAGE:
                self.save_image_metadata(data)

        # print(f'Saving the following cursor positions : {self.meta_info_list} to cursor_positions.json')
        # with open('cursor_positions.json', 'w') as convert_file:
        #     convert_file.write(json.dumps(self.meta_info_list))

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

    def save_image_metadata(self, name):
        if name:
            self.meta_info_list.append(ImageMetaData(variable_name=name))


if __name__ == '__main__':
    locator = InteractivePositionLocator(output_file='sample', save_key='alt+s', cursor_record_key='alt+r')
    locator.grab_cursor_positions()
