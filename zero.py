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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 0, 581, 481))
        self.verticalLayoutWidget.resize(110, 500)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(300, 0, 581, 481))
        self.verticalLayoutWidget2.resize(110, 500)
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout3")
        self.verticalLayoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget3.setGeometry(QtCore.QRect(10, 0, 581, 481))
        self.verticalLayoutWidget3.resize(200, 500)
        self.verticalLayoutWidget3.setObjectName("verticalLayoutWidget3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget3)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayout2")
        font = QtGui.QFont()
        font.setPointSize(9)




        for evnt in self.list_action:
            cbbxF = QtWidgets.QComboBox(self.verticalLayoutWidget)
            cbbxF.setFont(font)
            cbbxF.setGeometry(QtCore.QRect(650, 90, 115, 26))
            cbbxF.addItem("")
            cbbxF.addItem("")
            cbbxF.addItem("")
            self.list_cbbxF.append(cbbxF)
            self.verticalLayout.addWidget(cbbxF)

            cbbxC = QtWidgets.QComboBox(self.verticalLayoutWidget2)
            cbbxC.setFont(font)
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
            Label.setFont(font)
            Label.setGeometry(QtCore.QRect(390, 100, 67, 16))
            Label.setText("")
            self.list_label.append(Label)
            self.verticalLayout3.addWidget(Label)

        #FenetreG.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FenetreG)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menuFenetreG = QtWidgets.QMenu(self.menubar)
        self.menuFenetreG.setObjectName("menuFenetreG")
        #FenetreG.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FenetreG)
        self.statusbar.setObjectName("statusbar")
        #FenetreG.setStatusBar(self.statusbar)
        self.menuFenetreG.addSeparator()
        self.menubar.addAction(self.menuFenetreG.menuAction())

        self.retranslateUi(FenetreG)
        QtCore.QMetaObject.connectSlotsByName(FenetreG)


    def retranslateUi(self, FenetreG):
        _translate = QtCore.QCoreApplication.translate
        FenetreG.setWindowTitle(_translate("FenetreG", "Select preferences"))
        k=0
        L=[]
        for point in self.action:
            if point.action not in L:
                L.append(point.action)
                self.list_cbbxF[k].setItemText(0, _translate("FenetreG", "Ellipse"))
                self.list_cbbxF[k].setItemText(1, _translate("FenetreG", "Circle"))
                self.list_cbbxF[k].setItemText(2, _translate("FenetreG", "Rectangle"))
                self.list_cbbxC[k].setItemText(0, _translate("FenetreG", "red"))
                self.list_cbbxC[k].setItemText(1, _translate("FenetreG", "orange"))
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
                self.list_label[k].setText(_translate("FenetreG", L[k]))
                k+=1

    """def color(self):
        colour={}
        k = 0
        for point in self.action:
            if point.action not in colour:
                colour[point.action] = self.list_cbbxC[k].currentText()
                k += 1
        for j in range(len(colour)):
            self.list_cbbxC[j].currentTextChanged.connect(lambda: self.changedC(self.list_action[j],self.list_cbbxC[j]))
        return colour


    def changedC(self,name,evnt):
        colour= self.color()
        colour[name]=evnt.currentText()"""

def colour(ui):
    colour = {}
    k=0
    for point in ui.action:
        if point.action not in colour:
            colour[point.action] = ui.list_cbbxC[k].currentText()
            k += 1
    for j in range(len(colour)):
        ui.list_cbbxC[j].currentTextChanged.connect(lambda: changedC(ui,ui.list_action[j], ui.list_cbbxC[j]))
    return colour

def changedC(ui,name, evnt):
    col = colour(ui)
    col[name] = evnt.currentText()

    """def form(self):
        forms={}
        k = 0
        for point in self.action:
            if point.action not in forms:
                forms[point.action] = self.list_cbbxF[k].currentText()
                k += 1
        for j in range(len(forms)):
            self.list_cbbxF[j].currentTextChanged.connect(lambda: self.changedF(self.list_action[j],self.list_cbbxF[j]))
        return forms


    def changedF(self,name,evnt):
        forms= self.form()
        forms[name]=evnt.currentText()"""

def form(ui):
    forms = {}
    k = 0
    for point in ui.action:
        if point.action not in forms:
            forms[point.action] = ui.list_cbbxF[k].currentText()
            k += 1
    for j in range(len(forms)):
        ui.list_cbbxF[j].currentTextChanged.connect(lambda: changedF(ui,ui.list_action[j], ui.list_cbbxF[j]))
    return forms


def changedF(ui, name, evnt):
    forms=form(ui)
    forms[name] = evnt.currentText()
    print(forms)


if __name__ == "__main__":
    act = lect_fichier.load_actions('essai_donnees_2.txt')
    app = QtWidgets.QApplication(sys.argv)
    FenetreG = QtWidgets.QMainWindow()
    ui = Ui_FenetreG(act)
    ui.setupUi(FenetreG)
    print(colour(ui))
    print(form(ui))
    FenetreG.show()
    sys.exit(app.exec_())