# This Python file uses the following encoding: utf-8
import sys
import os
MAX_WIDTH = 1050
MAX_HEIGHT = 1000

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from form import Ui_MainWindow


if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # init
    Dialog = QtWidgets.QDialog()
    widget = Ui_MainWindow()
    widget.setupUi(Dialog)
    Dialog.setWindowTitle("The best messenger!")
    Dialog.setWindowIcon(QIcon("my_messenger_logo.png"))
    Dialog.setFixedSize(MAX_WIDTH, MAX_HEIGHT)
    Dialog.show()

    # Main loop
    sys.exit(app.exec_())
