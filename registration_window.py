# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(370, 218)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegistrationWindow.sizePolicy().hasHeightForWidth())
        RegistrationWindow.setSizePolicy(sizePolicy)
        RegistrationWindow.setStyleSheet("QWidget{ background-color: #f4f6ec; }")
        self.verticalLayout = QtWidgets.QVBoxLayout(RegistrationWindow)
        self.verticalLayout.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(RegistrationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{ color: #2d0c03; }")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(RegistrationWindow)
        self.lineEdit.setMinimumSize(QtCore.QSize(30, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 25))
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "color: #f4f6ec;\n"
                                    "background-color: #2d0c03;\n"
                                    "border: none;\n"
                                    "}")
        self.lineEdit.setMaxLength(30)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(RegistrationWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{ color: #2d0c03; }")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.registrationButton = QtWidgets.QPushButton(RegistrationWindow)
        self.registrationButton.setMinimumSize(QtCore.QSize(100, 25))
        self.registrationButton.setBaseSize(QtCore.QSize(35, 20))
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setBold(False)
        font.setWeight(50)
        self.registrationButton.setFont(font)
        self.registrationButton.setStyleSheet("QPushButton{ \n"
                                              "color: #f4f6ec;\n"
                                              "background-color: #ac0e28;\n"
                                              "border-radius: 10px;\n"
                                              "border: none;\n"
                                              " }\n"
                                              "QPushButton:focus:pressed { color:#2d0c03;  }\n"
                                              "QPushButton:hover {  background-color: #bc4558; }")
        self.registrationButton.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.registrationButton)
        self.cancelButton = QtWidgets.QPushButton(RegistrationWindow)
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 25))
        self.cancelButton.setBaseSize(QtCore.QSize(35, 20))
        font = QtGui.QFont()
        font.setFamily("STIXGeneral")
        font.setBold(False)
        font.setWeight(50)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{ \n"
                                        "color: #f4f6ec;\n"
                                        "background-color: #ac0e28;\n"
                                        "border-radius: 10px;\n"
                                        "border: none;\n"
                                        " }\n"
                                        "QPushButton:focus:pressed { color:#2d0c03;  }\n"
                                        "QPushButton:hover {  background-color: #bc4558; }")
        self.cancelButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(3, 2)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Registration Window"))
        self.label_2.setText(_translate("RegistrationWindow", "Fill in the registration fields:"))
        self.label.setText(_translate("RegistrationWindow", "Name of Login:"))
        self.registrationButton.setText(_translate("RegistrationWindow", "Register"))
        self.cancelButton.setText(_translate("RegistrationWindow", "Cancel"))

        # buttons logic
        self.cancelButton.clicked.connect(RegistrationWindow.close)
        # self.registrationButton.clicked.connect(self.register_user)
