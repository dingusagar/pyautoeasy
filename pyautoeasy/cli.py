import argparse

from tabulate import tabulate

from pyautoeasy import InteractivePositionLocator


def get_args():
    main_parser = argparse.ArgumentParser(prog='pyautoeasy', usage='%(prog)s --locate --output sample')
    main_parser.add_argument('-o', '--output', default='sample', help='File name of the generated sample program')
    main_parser.add_argument('--cursor-record-key', default='alt+r',
                             help='Records the current position of cursor and prompts for a meaningful name for this location.')
    main_parser.add_argument('--save-key', default='alt+s',
                             help='saves the recorded cursor positions and generates a sample program')
    args = main_parser.parse_args()
    return args


def display_intro(args):
    text = f"""
        Running Interactive pyautoeasy...
        
    Press {args.cursor_record_key} to record a cursor position 
    Press {args.save_key} to save and generate sample program 
    """
    table = [[text]]
    output = tabulate(table, tablefmt='grid')
    print(output)


def main():
    args = get_args()
    display_intro(args)
    locator = InteractivePositionLocator(output_file=args.output, save_key=args.save_key,
                                         cursor_record_key=args.cursor_record_key)
    locator.grab_cursor_positions()

if __name__ == '__main__':
    main()
