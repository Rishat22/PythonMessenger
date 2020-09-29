# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import QtWidgets, QtCore
from PySide2.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from main_window import Ui_MainWindow

MAX_WIDTH = 700
MAX_HEIGHT = 800

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)

    # init
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowFlags(QtCore.Qt.Window)
    widget = Ui_MainWindow()
    widget.setupUi(Dialog)
    Dialog.setWindowTitle("The best messenger!")
    Dialog.setWindowIcon(QIcon("my_messenger_logo.png"))
    Dialog.setMinimumSize(MAX_WIDTH / 2, MAX_HEIGHT / 2)
    Dialog.setMaximumSize(MAX_WIDTH, MAX_HEIGHT)
    Dialog.show()

    # Main loop
    sys.exit(app.exec_())
