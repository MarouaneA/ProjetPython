from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import lect_fichier

FICHIER = "essai_donnees.txt"
FICHIER_2 = "essai_donnees_2.txt"



class Config(object):

    def __init__(self, fichier):
        self.list_chkbx = []   # liste des Checkbox créées qui contiennent les différentes actions
        self.list_chkbx_join1 = []   # liste 1 des Checkbox créées pour faire des 'join'
        self.list_chkbx_join2 = []   # liste 2 des Checkbox créées pour faire des 'join'
        self.list_action_diff = lect_fichier.load_actions(fichier)[1]  # liste des actions differentes sous forme de str
        self.selec = initialisation(self)
        self.selec_join = initialisation(self)
        self.selec_join2 = initialisation(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # créer des checkbox pour la selection des actions
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 400, 550))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("select")
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)
        for evnt in self.list_action_diff:
            chkbx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            chkbx.setObjectName(evnt)
            chkbx.toggle()  # initialise l'état de la Checkbox à 'sélectionnée'
            # state (1er argument) : argument obligatoire de la méthode stateChanged + nécessité de mettre chkbx=chkbx
            # sinon la fonction n'évalue que le dernier de la boucle 'for' ( il faut définir des variables indépendantes)
            chkbx.stateChanged.connect(lambda state=0, evnt=evnt : dict_evnt(self,state,evnt))
            self.list_chkbx.append(chkbx)
            self.verticalLayout.addWidget(chkbx)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton("Save Configuration", self.horizontalLayoutWidget)
        self.pushButton_save.clicked.connect(lambda : self.save())
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_load = QtWidgets.QPushButton("Load Configuration", self.horizontalLayoutWidget)
        self.pushButton_load.clicked.connect(lambda : self.load())
        self.horizontalLayout.addWidget(self.pushButton_load)

        self.verticalLayout.addWidget(self.horizontalLayoutWidget)
        # mixe les actions selectionner : join
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 40, 90, 550))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("join")
        self.label_2.setFont(font)
        self.verticalLayout_2.addWidget(self.label_2)
        for evnt in self.list_action_diff:
            chkbx = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
            chkbx.setObjectName(evnt)
            # state (1er argument) : argument obligatoire de la méthode stateChanged + nécessité de mettre chkbx=chkbx
            # sinon la fonction n'évalue que le dernier de la boucle 'for' ( il faut définir des variables indépendantes)
            chkbx.stateChanged.connect(lambda state=0, evnt=evnt : dict_join(self,self.selec_join ,state,evnt))
            self.list_chkbx_join1.append(chkbx)
            self.verticalLayout_2.addWidget(chkbx)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_join = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_join.setObjectName("buttonjoin")
        self.pushButton_join.clicked.connect(lambda : reset_join1(self))
        self.horizontalLayout.addWidget(self.pushButton_join)
        self.verticalLayout_2.addWidget(self.horizontalLayoutWidget)

        # autre : mixe les actions selectionner : join
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(570, 40, 90, 550))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout3")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("join")
        self.label_3.setFont(font)
        self.verticalLayout_3.addWidget(self.label_3)
        for evnt in self.list_action_diff:
            chkbx = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
            chkbx.setObjectName(evnt)
            # state (1er argument) : argument obligatoire de la méthode stateChanged + nécessité de mettre chkbx=chkbx
            # sinon la fonction n'évalue que le dernier de la boucle 'for' ( il faut définir des variables indépendantes)
            chkbx.stateChanged.connect(lambda state=0, evnt=evnt: dict_join(self, self.selec_join2, state, evnt))
            self.list_chkbx_join2.append(chkbx)
            self.verticalLayout_3.addWidget(chkbx)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_join2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_join2.setObjectName("buttonjoin")
        self.pushButton_join2.clicked.connect(lambda : reset_join2(self))
        self.horizontalLayout.addWidget(self.pushButton_join2)
        self.verticalLayout_3.addWidget(self.horizontalLayoutWidget)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Select Configuration"))
        for k in range(len(self.list_action_diff)):
            self.list_chkbx[k].setText(_translate("MainWindow", self.list_action_diff[k]))
        self.pushButton_save.setText(_translate("MainWindow", "Save Configuration"))
        self.pushButton_load.setText(_translate("MainWindow", "Load Configuration"))
        self.pushButton_join.setText(_translate("MainWindow", "Reset"))
        self.pushButton_join2.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", 'Select action'))
        self.label_2.setText(_translate("MainWindow", 'Join action'))
        self.label_3.setText(_translate("MainWindow", 'Join action'))

    def setView(self, view):
        self.view = view

    def save(self):
        '''sauvegarde une configuration de la sélection d'action dans un fichier txt'''
        fileName = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, 'Dialog Title', './')
        if fileName:
            nom_fichier = fileName[0].split('/')[-1]
            fic = open(str(nom_fichier), 'w')
            for evnt in self.list_action_diff:
                # écrit : 'action  selected/deselected'
                fic.write(str(evnt)+'    '+self.selec[evnt]+'\n')
            fic.close()

    def load(self):
        '''importe une configuration de la sélection d'action dans un fichier txt,
        renvoi une erreur si on essai d'importer une configuration d'un autre fichier'''
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open file', '/home')

        dic = {}
        list_sel, list_unsel = [], []
        k = 0
        pb = 0

        if fname[0]:
            nom_fichier = fname[0].split('/')[-1]
            with open(nom_fichier, 'r') as f:
                for line in f:
                    list = line.split()
                    if list[0] != self.list_action_diff[k]:
                        pb = 1 # relève un problème qui signifie que ce n'est pas le bon fichier
                    else :
                        dic[list[0]] = list[1]
                        if list[1] == 'selected':
                            list_sel.append(self.list_chkbx[k]) # liste des checkbox selectionnées
                        else:
                            list_unsel.append(self.list_chkbx[k]) # # liste des checkbox déselectionnées
                    k += 1
            if pb == 0 : # cad pas de problème de fichier
                # on change l'état des checkbox après la lecture du fichier pour ne pas modifier en cas de problème
                for chkbx in list_sel :
                    chkbx.setChecked(True)
                for chkbx in list_unsel :
                    chkbx.setChecked(False)
                self.selec = dic
            else :
                print('Selection no load because it is not the selection of the right file')



def initialisation(ui):
    '''initialise un dictionnaire qui, à chaque action, renvoi 'selected' '''
    selec={}
    for action in ui.list_action_diff:
        selec[action]="selected"
    return selec


def dict_evnt(ui, state, evnt):
    '''change le dictionnaire 'selec_join' des actions , selon 'state',
    defini : dict[evnt] = selected (= 2) / deselected(= 0)'''
    if state == 0 :
        ui.selec[evnt] = "deselected"
    else :
        ui.selec[evnt] = "selected"

    ui.view.draw_timeline()


def dict_join(ui,selec_joini, state, evnt):
    '''change le dictionnaire 'selec_join' des actions , selon 'state',
    defini : dict[evnt] = join (= 2) / selected(= 0)'''
    if state == 2 :
        selec_joini[evnt] = 'join'
    else :
        selec_joini[evnt] = 'selected'
    ui.view.draw_timeline()

def reset_join1(ui):
    '''Reset l'état des checkbox de la 1ère sélection à déselctionner pour les 'join', enlève les jointures'''
    for k, chkbx in enumerate(ui.list_chkbx_join1):
       if chkbx.checkState() == 2:
            chkbx.setChecked(False)
            # si on a besoin de récupérer l'état des checkbox(première version)
            # ui.selec_join[ui.list_action_diff[k]] = "selected"


def reset_join2(ui):
    '''Reset l'état des checkbox de la 2ème sélection à déselctionner pour les 'join', enlève les jointures'''
    for k, chkbx in enumerate(ui.list_chkbx_join2):
       if chkbx.checkState() == 2:
            chkbx.setChecked(False)
            # si on a besoin de récupérer l'état des checkbox(première version)
            # ui.selec_join2[ui.list_action_diff[k]] = "selected"


if __name__ == "__main__":
    fichier = FICHIER
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui2 = Config(fichier)
    ui2.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

