from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lect_fichier
import configuration


class Ui_FenetreG(object):

    def __init__(self, act):
        self.action = act
        self.list_cbbxF = []   # liste des Combobox des différentes formes
        self.list_cbbxC = []   # liste des Combobox des différentes couleurs
        self.list_action = configuration.list_action(self.action)  # liste des actions sous forme de str
        self.list_label = []   # liste des Labels

    def setupUi(self, FenetreG):
        FenetreG.setObjectName("FenetreG")
        FenetreG.resize(600, 800)
        FenetreG.setEnabled(True)
        self.centralwidget = QtWidgets.QWidget(FenetreG)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 0, 581, 481))
        self.verticalLayoutWidget.resize(110, 600)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(400, 0, 581, 481))
        self.verticalLayoutWidget2.resize(110, 600)
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout3")
        self.verticalLayoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget3.setGeometry(QtCore.QRect(10, 0, 581, 481))
        self.verticalLayoutWidget3.resize(280, 600)
        self.verticalLayoutWidget3.setObjectName("verticalLayoutWidget3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget3)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayout2")



        for evnt in self.list_action:
            cbbxF = QtWidgets.QComboBox(self.verticalLayoutWidget)
            cbbxF.setGeometry(QtCore.QRect(650, 90, 115, 26))
            cbbxF.addItem("")
            cbbxF.addItem("")
            cbbxF.addItem("")
            self.list_cbbxF.append(cbbxF)
            self.verticalLayout.addWidget(cbbxF)

            cbbxC = QtWidgets.QComboBox(self.verticalLayoutWidget2)
            cbbxC.setGeometry(QtCore.QRect(220, 50, 91, 26))
            cbbxC.setAutoFillBackground(False)
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            cbbxC.addItem("")
            self.list_cbbxC.append(cbbxC)
            self.verticalLayout2.addWidget(cbbxC)

            Label = QtWidgets.QLabel(self.verticalLayoutWidget3)
            Label.setGeometry(QtCore.QRect(390, 100, 67, 16))
            Label.setText("")
            self.list_label.append(Label)
            self.verticalLayout3.addWidget(Label)




        FenetreG.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FenetreG)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuFenetreG = QtWidgets.QMenu(self.menubar)
        self.menuFenetreG.setObjectName("menuFenetreG")
        FenetreG.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FenetreG)
        self.statusbar.setObjectName("statusbar")
        FenetreG.setStatusBar(self.statusbar)
        self.menuFenetreG.addSeparator()
        self.menubar.addAction(self.menuFenetreG.menuAction())

        self.retranslateUi(FenetreG)
        QtCore.QMetaObject.connectSlotsByName(FenetreG)


    def retranslateUi(self, FenetreG):
        _translate = QtCore.QCoreApplication.translate
        FenetreG.setWindowTitle(_translate("FenetreG", "Select preferences"))
        for k in range(len(self.list_action)):
            self.list_cbbxF[k].setItemText(0, _translate("FenetreG", "Ellipse"))
            self.list_cbbxF[k].setItemText(1, _translate("FenetreG", "Circle"))
            self.list_cbbxF[k].setItemText(2, _translate("FenetreG", "Rectangle"))
            self.list_cbbxC[k].setItemText(0, _translate("FenetreG", "orange"))
            self.list_cbbxC[k].setItemText(1, _translate("FenetreG", "red"))
            self.list_cbbxC[k].setItemText(2, _translate("FenetreG", "blue"))
            self.list_cbbxC[k].setItemText(3, _translate("FenetreG", "green"))
            self.list_cbbxC[k].setItemText(4, _translate("FenetreG", "magenta"))
            self.list_cbbxC[k].setItemText(5, _translate("FenetreG", "cyan"))
            self.list_cbbxC[k].setItemText(6, _translate("FenetreG", "lime"))
            self.list_cbbxC[k].setItemText(7, _translate("FenetreG", "purple"))
            self.list_cbbxC[k].setItemText(8, _translate("FenetreG", "silver"))
            self.list_cbbxC[k].setItemText(9, _translate("FenetreG", "indigo"))
            self.list_cbbxC[k].setItemText(10, _translate("FenetreG", "maroon"))
            self.list_cbbxC[k].setItemText(11, _translate("FenetreG", "olive"))
            self.list_cbbxC[k].setItemText(12, _translate("FenetreG", "navy"))
            self.list_cbbxC[k].setItemText(13, _translate("FenetreG", "goldenrhod"))
            self.list_cbbxC[k].setItemText(14, _translate("FenetreG", "teal"))
            self.list_cbbxC[k].setItemText(15, _translate("FenetreG", "darkorange"))
            self.list_cbbxC[k].setItemText(16, _translate("FenetreG", "crimson"))
            self.list_cbbxC[k].setItemText(17, _translate("FenetreG", "seagreen"))
            self.list_cbbxC[k].setItemText(18, _translate("FenetreG", "steelblue"))
            self.list_cbbxC[k].setItemText(19, _translate("FenetreG", "lightcoral"))
            self.list_cbbxC[k].setItemText(20, _translate("FenetreG", "grey"))
            self.list_cbbxC[k].setItemText(21, _translate("FenetreG", "black"))
            self.list_cbbxC[k].setItemText(22, _translate("FenetreG", "orangered"))
            self.list_label[k].setText(_translate("FenetreG", self.list_action[k]))


if __name__ == "__main__":
    act = lect_fichier.load_actions("essai_donnees.txt")
    app = QtWidgets.QApplication(sys.argv)
    FenetreG = QtWidgets.QMainWindow()
    ui = Ui_FenetreG(act)
    ui.setupUi(FenetreG)
    FenetreG.show()
    sys.exit(app.exec_())