from queue import Queue


class MESSAGE_TYPE:
    GRAB_IMAGE = 'GRAB_IMAGE'
    RECORD_POSITION = 'RECORD_POSITION'
    SAVE_AND_EXIT = 'SAVE_AND_EXIT'
    CAPTURED_IMAGE = 'CAPTURED_IMAGE'


message_queue = Queue()


def send_message(command, data=None):
    command_data_tuple = (command, data)
    message_queue.put(command_data_tuple)


def receive_message():
    return message_queue.get()
