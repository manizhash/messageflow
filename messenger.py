from datetime import datetime

import requests
from PyQt6 import QtWidgets, QtCore
from clientui import Ui_MainWindow


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def print_message(self, message):
        pass
    
    def get_messages(self):
        pass

    def send_message(self):
        pass


app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec()
