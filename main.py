# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from form import Ui_MainWindow
from registration_window import Ui_RegistrationWindow

MAX_WIDTH = 700
MAX_HEIGHT = 800


def open_registration_window(self):
    registration_window = QtWidgets.QWidget(self)
    registration_widget = Ui_RegistrationWindow()
    registration_widget.setupUi(registration_window)
    registration_window.show()


def open_login_window():
    print('Hello')


if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # init
    Dialog = QtWidgets.QDialog()
    widget = Ui_MainWindow()
    widget.setupUi(Dialog)
    Dialog.setWindowTitle("The best messenger!")
    Dialog.setWindowIcon(QIcon("my_messenger_logo.png"))
    Dialog.setMinimumSize(MAX_WIDTH / 2, MAX_HEIGHT / 2)
    Dialog.setMaximumSize(MAX_WIDTH, MAX_HEIGHT)
    Dialog.show()

    # buttons logic
    widget.loginButton.clicked.connect(open_login_window)
    widget.registrationButton.clicked.connect(open_registration_window)

    # Main loop
    sys.exit(app.exec_())
