# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 850))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.starterButton = QtWidgets.QPushButton(self.centralwidget)
        self.starterButton.setGeometry(QtCore.QRect(990, 360, 180, 50))
        self.starterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.starterButton.setObjectName("starterButton")
        self.payoffsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.payoffsTable.setGeometry(QtCore.QRect(460, 20, 711, 330))
        self.payoffsTable.setStyleSheet("")
        self.payoffsTable.setObjectName("payoffsTable")
        self.payoffsTable.setColumnCount(0)
        self.payoffsTable.setRowCount(0)
        self.payoffsTable.horizontalHeader().setVisible(False)
        self.payoffsTable.verticalHeader().setVisible(False)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(460, 360, 180, 50))
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setObjectName("resetButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 500, 391, 311))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.r1 = QtWidgets.QRadioButton(self.groupBox)
        self.r1.setGeometry(QtCore.QRect(20, 70, 351, 31))
        self.r1.setChecked(True)
        self.r1.setObjectName("r1")
        self.r3 = QtWidgets.QRadioButton(self.groupBox)
        self.r3.setGeometry(QtCore.QRect(20, 170, 291, 21))
        self.r3.setShortcut("")
        self.r3.setCheckable(True)
        self.r3.setChecked(False)
        self.r3.setAutoExclusive(True)
        self.r3.setObjectName("r3")
        self.results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(460, 500, 711, 330))
        self.results.setMaximumSize(QtCore.QSize(797, 591))
        self.results.setReadOnly(True)
        self.results.setObjectName("results")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 291, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 291, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.nbStr1 = QtWidgets.QSpinBox(self.centralwidget)
        self.nbStr1.setGeometry(QtCore.QRect(150, 80, 120, 30))
        self.nbStr1.setReadOnly(False)
        self.nbStr1.setMinimum(1)
        self.nbStr1.setMaximum(3)
        self.nbStr1.setObjectName("nbStr1")
        self.nbStr2 = QtWidgets.QSpinBox(self.centralwidget)
        self.nbStr2.setGeometry(QtCore.QRect(150, 220, 120, 30))
        self.nbStr2.setReadOnly(False)
        self.nbStr2.setMinimum(1)
        self.nbStr2.setMaximum(3)
        self.nbStr2.setObjectName("nbStr2")
        self.checkZS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkZS.setGeometry(QtCore.QRect(80, 280, 261, 71))
        self.checkZS.setCheckable(True)
        self.checkZS.setChecked(False)
        self.checkZS.setAutoRepeat(False)
        self.checkZS.setAutoExclusive(False)
        self.checkZS.setTristate(False)
        self.checkZS.setObjectName("checkZS")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mixed Strategies"))
        self.starterButton.setText(_translate("MainWindow", "Start Game"))
        self.resetButton.setText(_translate("MainWindow", "Reset Game"))
        self.groupBox.setTitle(_translate("MainWindow", "Results to view"))
        self.r1.setText(_translate("MainWindow", "Nash Equilibriums"))
        self.r3.setText(_translate("MainWindow", "Value"))
        self.label.setText(_translate("MainWindow", "Player1\'s strategies"))
        self.label_2.setText(_translate("MainWindow", "Player2\'s strategies"))
        self.checkZS.setText(_translate("MainWindow", "Zero-Sum Game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
