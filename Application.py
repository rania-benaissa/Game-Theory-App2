from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QLineEdit, QInputDialog, QStyledItemDelegate, QMessageBox
from Interface import Ui_MainWindow  # importing our generated file
from PyQt5 import QtCore, QtWidgets
import sys
import numpy as np
from Game import Game
from Player import Player
import qdarkstyle
from PyQt5.Qt import QFont
import re


class CenterDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QStyledItemDelegate.createEditor(self, parent, option, index)
        editor.setAlignment(QtCore.Qt.AlignCenter)

        font = QFont("Century Gothic", 12)
        font.setBold(True)
        editor.setFont(font)
        return editor


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        # app settings
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # creates a font
        self.font = QFont("Century Gothic", 12)
        self.font.setBold(True)

        # INITIALISATIONS
        self.resetGame()

        # disable spinners + make them listen
        self.ui.nbStr1.lineEdit().setReadOnly(True)
        self.ui.nbStr2.lineEdit().setReadOnly(True)

        # set my style sheet
        self.setFont(self.font)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.ui.payoffsTable.setItemDelegate(CenterDelegate())

        # SIGNALS
        self.ui.nbStr1.valueChanged.connect(
            lambda: self.changeStrategies(self.ui.nbStr1))

        self.ui.nbStr2.valueChanged.connect(
            lambda: self.changeStrategies(self.ui.nbStr2))

        self.ui.starterButton.clicked.connect(self.lunchGame)

        self.ui.resetButton.clicked.connect(self.resetGame)

        self.activateRadios()

        self.ui.payoffsTable.cellChanged.connect(
            lambda i, j: self.changeFont(i, j, self.ui.payoffsTable))

        self.ui.checkZS.stateChanged.connect(self.changeGame)

    def changeFont(self, i, j, table):

        table.item(i, j).setFont(self.font)

    def activateRadios(self):

        self.ui.r1.toggled.connect(lambda: self.updateResults(self.ui.r1))
        self.ui.r3.toggled.connect(lambda: self.updateResults(self.ui.r3))

    # change the strategie's number of a player
    def changeStrategies(self, spinner):

        payTable = self.ui.payoffsTable

        value = spinner.value()

        if spinner.objectName() == "nbStr1":

            if value + 1 >= payTable.rowCount():

                payTable.setRowCount(payTable.rowCount()+1)

                payTable.setItem(
                    value, 0, QTableWidgetItem("Strategy " + str(value)))

                payTable.item(value, 0).setFont(self.font)
                payTable.item(value, 0).setTextAlignment(
                    QtCore.Qt.AlignCenter)

                for i in range(1, payTable.columnCount()):
                    if(not self.ui.checkZS.isChecked()):
                        payTable.setItem(value, i, QTableWidgetItem("(  ,  )"))
                    else:
                        payTable.setItem(value, i, QTableWidgetItem(""))
                    payTable.item(value, i).setFont(self.font)

            else:
                payTable.removeRow(payTable.rowCount() - 1)

        else:

            if value + 1 >= payTable.columnCount():

                payTable.setColumnCount(payTable.columnCount() + 1)

                payTable.setItem(
                    0,  value, QTableWidgetItem("Strategy " + str(value)))

                payTable.item(0, value).setFont(self.font)
                payTable.item(0, value).setTextAlignment(
                    QtCore.Qt.AlignCenter)

                for i in range(1, payTable.rowCount()):

                    if(not self.ui.checkZS.isChecked()):
                        payTable.setItem(i, value, QTableWidgetItem("(  ,  )"))
                    else:
                        payTable.setItem(i, value, QTableWidgetItem(""))
                    payTable.item(i, value).setFont(self.font)

            else:
                payTable.removeColumn(payTable.columnCount() - 1)

        self.alignTable()

    def createPayoffsTable(self, table):

        # setting shape

        table.setRowCount(2)

        table.setColumnCount(2)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        table.horizontalHeader().setStretchLastSection(True)

        # set init cells
        table.setItem(0, 0, QTableWidgetItem("Player1 | Player2"))
        table.setItem(0, 1, QTableWidgetItem("Strategy 1"))
        table.setItem(1, 0, QTableWidgetItem("Strategy 1"))
        table.setItem(1, 1, QTableWidgetItem(""))

        if(not self.ui.checkZS.isChecked()):

            table.setItem(1, 1, QTableWidgetItem("(  ,  )"))

        table.item(0, 0).setFont(self.font)
        table.item(0, 1).setFont(self.font)
        table.item(1, 0).setFont(self.font)
        table.item(1, 1).setFont(self.font)

        # rendre le 1er item inchangé
        item = table.item(0, 0)
        item.setFlags(QtCore.Qt.ItemIsEnabled)

        # centrer la table widget
        self.alignTable()

    def correctZeroSumProfiles(self):

        payTable = self.ui.payoffsTable

        for i in range(1,  payTable.rowCount()):

            for j in range(1, payTable.columnCount()):

                profile = str(payTable.item(i, j).text())
                profile = profile.replace(" ", "")

                regex = r'^[-+]?[0-9]+(\.[0-9]+)?$'

                if(not bool(re.match(regex, profile))):

                    QMessageBox.about(self, "Error detected",
                                      "Expected an integer or a float number.\nExemple : 11.5 , 12 , 0")

                    return False

        return True

    def correctProfiles(self):

        payTable = self.ui.payoffsTable

        for i in range(1, payTable.rowCount()):

            for j in range(1, payTable.columnCount()):

                profile = str(payTable.item(i, j).text())
                profile = profile.replace(" ", "")

                nb_commas = profile.count(",")

                dec = r'[-+]?[0-9]+(\.[0-9]+)?'
                regex = r'^\(' + dec + r'(,'+dec+r')+\)$'

                if(not bool(re.match(regex, profile)) or nb_commas != 1):

                    if(not bool(re.match(regex, profile))):

                        QMessageBox.about(self, "Error detected",
                                          "Syntax Error at row "+str(i))
                    else:
                        QMessageBox.about(self, "Error detected",
                                          "Incorrect payoffs number at row "+str(i))
                    return False

        return True

    def lunchGame(self):

        if(self.ui.checkZS.isChecked()):

            run = self.correctZeroSumProfiles()
        else:
            run = self.correctProfiles()

        if(run):
            str1 = []
            str2 = []

            profiles1 = []
            profiles2 = []

            payoffsTable = self.ui.payoffsTable

            for i in range(0, payoffsTable.rowCount()):

                profil1 = []
                profil2 = []

                # gotta get the profile of a player and convert its values to int

                for j in range(0, payoffsTable.columnCount()):

                    if(i == 0 and j != 0):
                        str2.append(payoffsTable.item(i, j).text())
                    if(j == 0 and i != 0):
                        str1.append(payoffsTable.item(i, j).text())

                    if(i != 0 and j != 0):

                        value = payoffsTable.item(i, j).text()

                        value = value.replace(")", "")
                        value = value.replace("(", "")
                        value = value.replace(" ", "")
                        profiles = value.split(",")

                        if not self.ui.checkZS.isChecked():
                            profil1.append(float(profiles[0]))
                            profil2.append(float(profiles[1]))
                        else:
                            profil1.append(float(profiles[0]))
                            profil2.append(-float(profiles[0]))

                if(i != 0):
                    profiles1.append(profil1)
                    profiles2.append(profil2)

            player1 = Player(str1, np.array(profiles1))

            player2 = Player(str2, np.array(profiles2))

            self.game = Game([player1, player2])

            # calculate nash equilibrium since it s already selected
            self.updateResults(self.ui.r1)

            # disable the profiles table + its button
            self.disableTable()
            self.ui.starterButton.setEnabled(False)
            self.ui.groupBox.setEnabled(True)
            self.ui.nbStr1.setEnabled(False)
            self.ui.nbStr2.setEnabled(False)
            self.ui.checkZS.setEnabled(False)

            if(self.ui.checkZS.isChecked()):

                self.ui.r3.setEnabled(True)
            else:
                self.ui.r3.setEnabled(False)

    def updateResults(self, radio):

        if radio.isChecked() is True:

            # clear the results screen
            self.ui.results.clear()

            if radio.objectName() == "r1":

                self.nash = self.game.supportEnumAlgo()

                if self.nash:

                    for element in self.nash:
                        self.ui.results.appendPlainText(
                            str(tuple(self.game.players[0].strategies)) + " , " +
                            str(tuple(self.game.players[1].strategies)) + " = " +
                            str(element[0]) + " , " + str(element[1]) + "\n")
                else:
                    self.ui.results.appendPlainText(
                        "There's no Nash equilibrium\n")

            if radio.objectName() == "r3":

                value = self.game.calculateValue(self.nash)
                self.ui.results.appendPlainText(
                    "The game's value is equal to : " + str(value) + "\n")

    # this will change tuples to one value
    def changeGame(self):

        table = self.ui.payoffsTable

        for i in range(1, table.rowCount()):

            for j in range(1, table.columnCount()):

                if self.ui.checkZS.isChecked():

                    table.setItem(i, j, QTableWidgetItem(""))
                else:
                    table.setItem(i, j, QTableWidgetItem("(  ,  )"))

                table.item(i, j).setFont(self.font)

        self.alignTable()

    def alignTable(self):

        table = self.ui.payoffsTable

        for i in range(0, table.rowCount()):

            for j in range(0, table.columnCount()):

                if(table.item(i, j)):

                    table.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

    def resetGame(self):

        # reset game's options
        self.game = None

        # enable widgets
        self.ui.nbStr1.setEnabled(True)
        self.ui.nbStr2.setEnabled(True)
        self.ui.checkZS.setEnabled(True)
        self.ui.checkZS.setChecked(False)
        self.ui.starterButton.setEnabled(True)

        # set strategies nb to 1
        self.ui.nbStr1.setValue(1)
        self.ui.nbStr2.setValue(1)

        # disable the radios
        self.ui.groupBox.setEnabled(False)

        # clear payoff table and create it back
        self.ui.payoffsTable.clear()
        self.createPayoffsTable(self.ui.payoffsTable)

        # clear plain text
        self.ui.results.clear()

    def disableTable(self):

        table = self.ui.payoffsTable

        for i in range(0, table.rowCount()):

            for j in range(0, table.columnCount()):

                item = table.item(i, j)
                item.setFlags(QtCore.Qt.ItemIsEnabled)


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
