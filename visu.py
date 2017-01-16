__author__ = 'aatefma'
import math



from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent




class View(QtWidgets.QWidget):

    def __init__(self, act,color_form,selec,selec_join,selec_join2):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action = act
        self.color_form = color_form
        self.selec= selec
        self.selec_join = selec_join
        self.selec_join2 = selec_join2
        self.grview = None
        self.scene = None
        self.entry = None
        self.build_interface()
        self.draw_timeline()
        self.dep_time = act[0].time
        self.valeur = 0
        self.premier=0


    @QtCore.pyqtSlot(int)
    def zoom_view(self, value):
        self.grview.scale(value, value)

    @QtCore.pyqtSlot(QWheelEvent)
    def zoom_view_mouse(self, event):
        self.grview.setTransformationAnchor(self.grview.AnchorUnderMouse)
        factor = math.pow(1.001, event.angleDelta().y())
        self.grview.scale(factor, factor)

    def zoom_time(self,value):
        self.draw_timeline(self,value)



    def build_interface(self):
        def add_button(text, slot):
            """adds a button to the hbox and connects the slot"""
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(slot)
            vbox.addWidget(button)
        slider = QtWidgets.QSlider()
        slider.setGeometry(QtCore.QRect(0, 0, 50, 800))
        slider.setOrientation(QtCore.Qt.Horizontal)
        slider.setObjectName("verticalScrollBar")
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
        vbox.addWidget(slider)
        self.draw_timeline()
        self.grview.fitInView(self.grview.sceneRect(), QtCore.Qt.KeepAspectRatio)
        add_button('Mise à jour', lambda: self.draw_timeline())
        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")

    def draw_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsRectItem()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        pen_black = QtGui.QPen(QtCore.Qt.black)
        pen_grey = QtGui.QPen(QtCore.Qt.gray)
        width = 60
        i = 2
        t_0 = self.action[0].time
        t_f = self.action[-1].time
        inter= (t_f - t_0)/2000
        dict={}
        for point in self.action:
            if self.selec[point.action] == 'selected':
                if self.selec_join[point.action] == 'join':
                    dict[point.action] = 0
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - t_0) / inter), y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys, inter), timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    font = QtGui.QFont()
                    font.setPointSize(30)
                    label.setFont(font)
                    label.setFont(font)
                    label_2.setFont(font)
                    label.setGeometry(-300, 100 * i,700, 40)
                    self.scene.addWidget(label)
                    label_2.setGeometry(inter * 8, 100 * i, 700, 40)
                    self.scene.addWidget(label_2)
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
                elif self.selec_join2[point.action] == 'join':
                    dict[point.action] = 1
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - t_0) / inter), y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys, inter), timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    font = QtGui.QFont()
                    font.setPointSize(30)
                    label.setFont(font)
                    label.setFont(font)
                    label_2.setFont(font)
                    label.setGeometry(-300, 100 * i, 700, 40)
                    self.scene.addWidget(label)
                    label_2.setGeometry(inter * 8, 100 * i, 700, 40)
                    self.scene.addWidget(label_2)
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
                elif point.action not in dict:
                    dict[point.action] = i
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - t_0) / inter), y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys, inter),timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    font = QtGui.QFont()
                    font.setPointSize(30)
                    label.setFont(font)
                    label.setFont(font)
                    label_2.setFont(font)
                    label.setGeometry(-800,100 * i,900,40)
                    self.scene.addWidget(label)
                    label_2.setGeometry(inter * 8, 100 * i, 700, 40)
                    self.scene.addWidget(label_2)
                    i+= 1

                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)
                else:
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    xys = ((point.time - t_0) / inter), 100 * dict[point.action]
                    if self.color_form[point.action][1] == 'Rectangle':
                        item = QtWidgets.QGraphicsRectItem(xy_coords(xys, width), timeline_group)
                    else:
                        item = QtWidgets.QGraphicsEllipseItem(xy_coords(xys, width), timeline_group)

                #Nécessaire pour que le timeline_group.hoverEnterEvent fonctionne
                item.setAcceptHoverEvents(True)
                def mouseEnterQGraphics(event, item = item, width = width, xys = xys):
                  item.setRect(xy_coords(xys, width * 5))
                def mouseExitQGraphics(event, item = item, width = width, xys = xys):
                  item.setRect(xy_coords(xys, width))

                item.hoverEnterEvent = mouseEnterQGraphics
                item.hoverLeaveEvent = mouseExitQGraphics

                item.setPen(pen_black)
                line.setPen(pen_grey)
                item.setBrush(brush)
                item.setToolTip(point.action+' '+ point.arg)


def xy_coords(xy, width):
    dw = width / 3
    return QtCore.QRectF(xy[0] - dw, xy[1]-dw/3, width/3, width/3)




def xy_line(xy, inter):
    return QtCore.QRectF(-50 , xy[1], (inter*8)+50, 1)