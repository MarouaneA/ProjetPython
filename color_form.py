
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lect_fichier


COLORS = ['red', 'orange', 'blue', 'green', 'magenta', 'cyan', 'lime', 'purple', 'silver', 'indigo', 'maroon',
          'olive', 'navy', 'goldenrod', 'teal', 'darkorange' 'crimson', 'seagreen', 'steelblue', 'lightcoral',
          'grey', 'orangered', 'black']

FORME = ['Circle', 'Rectangle']

FICHIER = 'essai_donnees.txt'


class Ui_MainWindow(object):

    def __init__(self, fichier):
        #self.action = lect_fichierbiss.load_actions(fichier)[0]
        self.list_action_differente = lect_fichier.load_actions(fichier)[1]  # liste des actions differentes sous forme de str

        self.list_label = []
        self.list_comboBox_form = []
        self.list_comboBox_colour = []
        self.selec_un=initialisation(self)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 800, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setPointSize(9)
        for action in self.list_action_differente:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout"+action)
        #text label
            self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.label.setObjectName("label"+action)
            self.label.setFont(font)
            self.list_label.append(self.label)
            self.horizontalLayout.addWidget(self.label)
        #combobox couleur
            self.comboBox_colour = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.comboBox_colour.setObjectName("comboBox_colour"+action)
            for k in range(len(COLORS)):
                self.comboBox_colour.addItem("")
            # 'state' contient le texte contenu dans dans la comboBox
            self.comboBox_colour.currentTextChanged.connect(lambda state, action=action : change_colour(self, state, action))
            self.horizontalLayout.addWidget(self.comboBox_colour)
            self.list_comboBox_colour.append(self.comboBox_colour)
        #combobox forme
            self.comboBox_form = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.comboBox_form.setObjectName("comboBox_form"+action)
            for k in range(len(FORME)):
                self.comboBox_form.addItem("")
            # 'state' contient le texte contenu dans dans la comboBox
            self.comboBox_form.currentTextChanged.connect(lambda state, action=action : change_form(self, state, action))
            self.horizontalLayout.addWidget(self.comboBox_form)
            self.list_comboBox_form.append(self.comboBox_form)

            self.verticalLayout.addLayout(self.horizontalLayout)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choix des couleurs et des formes"))
        for k in range(len(self.list_action_differente)):
            n = len(COLORS)
            r = k // n  #dicision euclidienne
            #print(n, k, r)
            self.list_label[k].setText(_translate("MainWindow", self.list_action_differente[k]))
            for i in range(k, n):
                    self.list_comboBox_colour[k].setItemText(i-k, _translate("MainWindow", COLORS[i%n]))
            for i in range(k):
                    self.list_comboBox_colour[k].setItemText(i+n-k, _translate("MainWindow", COLORS[i%n]))
            for j in range(len(FORME)):
                self.list_comboBox_form[k].setItemText(j, _translate("MainWindow", FORME[j]))


def initialisation(ui):
    selec_color_form={}
    k = 0
    for action in ui.list_action_differente:
        selec_color_form[action]=[COLORS[k%len(ui.list_action_differente)], FORME[0]]
        k+=1
    return selec_color_form

def change_colour(ui, state, action):
    ui.selec_un[action][0] = state
    #print(action, state)
    #print(ui.selec_un)

def change_form(ui, state, action):
    ui.selec_un[action][1] = state
    #print(action, state)
    #print(ui.selec_un)



if __name__ == "__main__":
    fichier = FICHIER
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(fichier)
    ui.setupUi(MainWindow)
    #print(initialisation(ui))
    MainWindow.show()
    sys.exit(app.exec_())