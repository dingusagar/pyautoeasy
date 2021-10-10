from pyautoeasy import InteractivePositionLocator

from pyautoeasy.__main__ import get_args


def main():
    args = get_args()
    locator = InteractivePositionLocator(output_file=args.output, save_key=args.save_key,
                                         cursor_record_key=args.cursor_record_key)
    locator.grab_cursor_positions()