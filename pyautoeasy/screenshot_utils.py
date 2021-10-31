import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
import pyscreenshot as ImageGrab
import numpy as np
import cv2
from PyQt5.QtWidgets import QInputDialog, QLineEdit
import os

from pyautoeasy.shared_queue import send_message, MESSAGE_TYPE

class ScreenShotWidget(QtWidgets.QWidget):
    def __init__(self, image_dir=os.path.curdir):
        super().__init__()
        self.image_dir = image_dir
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def prompt_input_dialog(self, title, message):
        text, okPressed = QInputDialog.getText(self, title, message, QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
            return text
        return None

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        cv2.imshow('Captured Image', img)

        image_name = self.prompt_input_dialog(title="Recording Image",
                                              message="Give a meaningful name for the Captured Image")

        if image_name:
            image_name = f'{image_name}.png'
            print(f'Saving image as {image_name}')
            image_path = os.path.join(self.image_dir, image_name)
            cv2.imwrite(image_path, img)
            send_message(MESSAGE_TYPE.CAPTURED_IMAGE, data=image_name)

        cv2.destroyAllWindows()


def take_screenshot(image_dir=None):
    if not image_dir:
        image_dir = os.path.curdir
    app = QtWidgets.QApplication(sys.argv)
    window = ScreenShotWidget(image_dir=image_dir)
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.exec_()
    # sys.exit(app.exec_())



if __name__ == '__main__':
    take_screenshot()
    print('Hello')
