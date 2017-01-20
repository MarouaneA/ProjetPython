
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import load_file


COLORS = ['red', 'orange', 'blue', 'green', 'magenta', 'cyan', 'lime', 'purple', 'silver', 'indigo', 'maroon',
          'olive', 'navy', 'goldenrod', 'teal', 'darkorange' 'crimson', 'seagreen', 'steelblue', 'lightcoral',
          'grey', 'orangered', 'black']

FORME = ['Circle', 'Rectangle']

FICHIER = 'essai_donnees.txt'


class Ui_MainWindow(object):

    def __init__(self, fichier):

        # liste des actions differentes sous forme de str
        self.list_action_differente = load_file.load_actions(fichier)[1]
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
        #création text label pour 'action'
            self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.label.setObjectName("label"+action)
            self.label.setFont(font)
            self.list_label.append(self.label)
            self.horizontalLayout.addWidget(self.label)
        #création combobox couleur pour 'action'
            self.comboBox_colour = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.comboBox_colour.setObjectName("comboBox_colour"+action)
            for k in range(len(COLORS)):
                self.comboBox_colour.addItem("")
            # 'state' contient le texte contenu dans dans la comboBox
            self.comboBox_colour.currentTextChanged.connect(lambda state, action=action : change_colour(self, state, action))
            self.horizontalLayout.addWidget(self.comboBox_colour)
            self.list_comboBox_colour.append(self.comboBox_colour)
        #création combobox forme pour 'action'
            self.comboBox_form = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.comboBox_form.setObjectName("comboBox_form"+action)
            for k in range(len(FORME)):
                self.comboBox_form.addItem("")
            # 'state' contient le texte contenu dans dans la comboBox
            self.comboBox_form.currentTextChanged.connect(lambda state, action=action : change_form(self, state, action))
            self.horizontalLayout.addWidget(self.comboBox_form)
            self.list_comboBox_form.append(self.comboBox_form)

            self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choix des couleurs et des formes"))
        for k in range(len(self.list_action_differente)):
            n = len(COLORS)
            self.list_label[k].setText(_translate("MainWindow", self.list_action_differente[k]))
            for i in range(k, n):
                self.list_comboBox_colour[k].setItemText(i-k, _translate("MainWindow", COLORS[i%n]))
            for i in range(k):
                self.list_comboBox_colour[k].setItemText(i+n-k, _translate("MainWindow", COLORS[i%n]))
            for j in range(len(FORME)):
                self.list_comboBox_form[k].setItemText(j, _translate("MainWindow", FORME[j]))

def initialisation(ui):
    '''initialise un dictionnaire qui, à chaque action, renvoie [sa couleur associée, sa forme associée]'''
    selec_color_form={}
    n = len(COLORS)
    for k, action in enumerate(ui.list_action_differente):
        selec_color_form[action]=[COLORS[k%n], FORME[0]]
    return selec_color_form

def change_colour(ui, state, action):
    '''change la couleur (= state) de l'action dans le dictionnaire selec_un'''
    ui.selec_un[action][0] = state

def change_form(ui, state, action):
    '''change la forme (= state) de l'action dans le dictionnaire selec_un'''
    ui.selec_un[action][1] = state


if __name__ == "__main__":
    fichier = FICHIER
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(fichier)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())