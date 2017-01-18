
import math
import datetime
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent




class View(QtWidgets.QWidget):

    def __init__(self, act,color_form,selec,selec_join,selec_join2):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action = act
        self.color_form = color_form
        self.dept_time = self.action[0].time
        self.final_time = self.action[-1].time
        self.inter = self.final_time - self.dept_time
        self.selec= selec
        self.selec_join = selec_join
        self.selec_join2 = selec_join2
        self.dict_visu = initialisation(act, self.selec,self.selec_join,self.selec_join2)
        self.grview = None
        self.scene = None
        self.entry = None
        self.build_interface()
        self.valeur = 0
        self.premier=0
        self.valeur_souris=1


    @QtCore.pyqtSlot(int)
    def zoom_view(self, value):
        self.grview.scale(value, value)

    @QtCore.pyqtSlot(QWheelEvent)
    def zoom_view_mouse(self, event):
        self.grview.setTransformationAnchor(self.grview.AnchorUnderMouse)
        factor = math.pow(1.001, event.angleDelta().y())
        self.grview.scale(factor, factor)
        self.valeur_souris=self.valeur_souris*factor

    #créé la fonction appellée par le bouton reset_zoom
    def reset_zoom(self):
        self.zoom_view(1/self.valeur_souris)
        self.valeur_souris=1
        self.draw_timeline()

    def build_interface(self):
        def add_button(text, slot):
            """adds a button to the hbox and connects the slot"""
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(slot)
            vbox.addWidget(button)

        # créé un slider
        slider = QtWidgets.QSlider()
        slider.setGeometry(QtCore.QRect(0, 0, 50, 800))
        slider.setOrientation(QtCore.Qt.Horizontal)
        slider.setObjectName("verticalScrollBar")

        # on créé la fonction lambda à laquelle on va connecter le slider
        def fonction_lambda(self,slider):
            if self.valeur ==0 and self.premier == 0 :
                self.valeur=slider.value()
                self.premier = 1
                self.valeur = slider.value()
                self.zoom_view((self.valeur+50)/50)
            else :
                self.zoom_view(1/((self.valeur+50)/50))
                self.valeur=slider.value()
                self.zoom_view((self.valeur+50)/50)

        # on connecte le slider à la fonction lambda
        slider.sliderReleased.connect(lambda: fonction_lambda(self,slider))
        vbox = QtWidgets.QVBoxLayout(self)
        self.grview = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene()
        self.grview.setScene(self.scene)
        self.grview.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.grview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.grview.wheelEvent = lambda event: self.zoom_view_mouse(event)
        self.grview.scale(1, 1)
        vbox.addWidget(self.grview)

        #on ajoute le slider au window
        vbox.addWidget(slider)

        #dessine la timeline
        self.draw_timeline()

        #recentre et redimensionne la timeline
        self.grview.fitInView(self.grview.sceneRect(),QtCore.Qt.KeepAspectRatio)
        self.zoom_view(1.60)

        # remet le zoom de la souris à la valeur initiale
        add_button('reset_zoom', lambda: self.reset_zoom())

        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")

    def draw_timeline(self):
        #nettoie la timeline
        self.scene.clear()

        #Création du groupe timeline_group, réunissant toutes les actions qui vont être représentées
        timeline_group = QtWidgets.QGraphicsRectItem()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)

        #mise en place des pen, et des valeurs initiales
        pen_black = QtGui.QPen(QtCore.Qt.black)
        pen_grey = QtGui.QPen(QtCore.Qt.gray)
        width = 40
        i = 2
        dict={}

        #dessin de la timeline:
        for point in self.action:
            if self.selec[point.action] == 'selected':

                #création de la première ligne correspondant aux actions jointes
                if self.selec_join[point.action] == 'join':
                    dict[point.action] = 0
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - self.dept_time) / (self.final_time - self.dept_time))*2000, y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys), timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    font = QtGui.QFont()
                    font.setPointSize(30)
                    label.setFont(font)
                    label_2.setFont(font)
                    label.setGeometry(-300, 100 * i,400, 40)
                    self.scene.addWidget(label)
                    label_2.setGeometry(2050, 100 * i, 400, 40)
                    self.scene.addWidget(label_2)
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)

                # création de la deuxième ligne correspondant aux actions jointes
                elif self.selec_join2[point.action] == 'join':
                    dict[point.action] = 1
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - self.dept_time) / self.inter)*2000, y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys), timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    label.setGeometry(-300, 100 * i, 700, 10)
                    self.scene.addWidget(label)
                    label_2.setGeometry(2050, 100 * i, 700, 10)
                    self.scene.addWidget(label_2)
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)

                # création d'une nouvelle ligne, dans le cas où l'action n'a toujours pas été représentée
                elif point.action not in dict:
                    dict[point.action] = i
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = (point.time - self.dept_time) / (self.final_time - self.dept_time)*2000, y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys),timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    font = QtGui.QFont()
                    font.setPointSize(50)
                    label.setStyleSheet('QLabel{background-color:white;color:black;}')
                    label.setFont(font)
                    label_2.setFont(font)
                    label_2.setStyleSheet('QLabel{background-color:white;color:black;}')
                    label.setGeometry(-1000,100 * i-30,950,40)
                    self.scene.addWidget(label)
                    label_2.setGeometry(2050, 100 * i-30, 950, 40)
                    self.scene.addWidget(label_2)
                    i+= 1

                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)

                #ajout d'un point sur une ligne déjà existante
                else:
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    xys = (point.time - self.dept_time) / (self.final_time - self.dept_time)*2000, 100 * dict[point.action]
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)

                #Nécessaire pour que le timeline_group.hoverEnterEvent fonctionne
                item.setAcceptHoverEvents(True)
                def mouseEnterQGraphics(event, item = item, width = width, xys = xys):
                  item.setRect(xy_coords_zoom(xys, width))
                def mouseExitQGraphics(event, item = item, width = width, xys = xys):
                  item.setRect(xy_coords(xys, width))
                item.hoverEnterEvent = mouseEnterQGraphics
                item.hoverLeaveEvent = mouseExitQGraphics
                item.setPen(pen_black)
                line.setPen(pen_grey)
                item.setBrush(brush)
                item.setToolTip(point.action+' '+ point.arg+' '+datetime.datetime.fromtimestamp(point.time/1000).strftime('%Y/%m/%d %H:%M:%S'))

    # Proposition d'une autre idée de dessin de la timeline, avec la création de nouveaux objets
    def draw_timeline_2(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsRectItem()
        self.scene.addItem(timeline_group)
        y = 0
        # dessine ligne par ligne
        for line in self.dict_visu:
            obj = Line(line,self.dict_visu[line],y,self.dept_time,self.final_time,self.color_form)
            obj.draw_line(timeline_group)
            y += 80


# création d'une classe ligne regroupant les points, le nom, et la position en y
class Line(object):
    def __init__(self,name,list_time_args,y, dept_time, final_time,color_form):
        self.name = name
        self.list_time_args = list_time_args
        self.y = y
        self.dept_time = dept_time
        self.final_time = final_time
        self.inter = self.final_time - self.dept_time
        self.color_form = color_form


    def draw_line(self,group):
        """dessin d'une ligne"""
        pen_black = QtGui.QPen(QtCore.Qt.black)
        pen_grey = QtGui.QPen(QtCore.Qt.gray)
        if self.name != 'selec_join' and self.name != 'selec_join_2':
            brush = QtGui.QBrush(QtGui.QColor(self.color_form[self.name][0]))
        label = QtWidgets.QLabel(self.name)
        font = QtGui.QFont()
        font.setPointSize(50)
        label.setGeometry(0,self.y ,900,40)
        line = QtWidgets.QGraphicsRectItem(QtCore.QRectF(0,self.y, 2000, 1), group)
        line.setPen(pen_grey)
        width = 60
        for point in self.list_time_args:
            xys = ((point[0] - self.dept_time)/self.inter)*2000, self.y
            if self.color_form[self.name][1] == 'Rectangle':
                item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), group)
            else:
                item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), group)
            item.setPen(pen_black)
            item.setBrush(brush)
            item.setToolTip(self.name + ' ' + point[1] + ' ' + datetime.datetime.fromtimestamp(point[0]/ 1000).strftime('%Y/%m/%d %H:%M:%S'))
            item.setAcceptHoverEvents(True)
            def mouseEnterQGraphics(event, item=item, width=width, xys=xys):
                item.setRect(xy_coords_zoom(xys, width))
            def mouseExitQGraphics(event, item=item, width=width, xys=xys):
                item.setRect(xy_coords(xys, width))
            item.hoverEnterEvent = mouseEnterQGraphics
            item.hoverLeaveEvent = mouseExitQGraphics

#création de dict_visu pour la deuxième méthode
def initialisation(act, selec, selec_join, selec_join_2):
    dict= {}
    for action in selec:
        if selec[action] == 'selected':
            dict[action] = []
    for point in act:
        dict[point.action].append((point.time,point.arg))
    for point in selec_join:
        dict['selec_join'] = []
        if selec_join[point] == 'join':
            dict[selec_join] += dict[point]
    for point in selec_join_2:
        dict['selec_join_2'] = []
        if selec_join_2[point] == 'join':
            dict[selec_join_2] += dict[point]
    return dict


def xy_coords(xy, width):
    """valeurs en position et en taille des points"""
    dw = width/2
    return QtCore.QRectF(xy[0] - dw, xy[1]- dw , width, width)

def xy_coords_zoom(xy, width):
    """valeurs en position et en taille des points lorsqu'on passe la souris dessus"""
    dw = width
    return QtCore.QRectF(xy[0]-dw, xy[1] -dw , 2*width, 2*width)


def xy_line(xy):
    """création d'une ligne"""
    return QtCore.QRectF(-50 , xy[1], 2050, 1)