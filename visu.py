__author__ = 'aatefma'
import math



from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QWheelEvent




class View(QtWidgets.QWidget):

    def __init__(self, act,color_form,selec):
        super(View, self).__init__()
        self.setWindowTitle('Timeline')
        self.action = act
        self.color_form = color_form
        self.selec= selec
        self.grview = None
        self.scene = None
        self.entry = None
        self.build_interface()
        self.draw_timeline()
        self.dep_time = act[0].time


    @QtCore.pyqtSlot(int)
    def zoom_view(self, value):
        self.grview.scale(value, 1)

    @QtCore.pyqtSlot(QWheelEvent)
    def zoom_view_mouse(self, event):
        self.grview.setTransformationAnchor(self.grview.AnchorUnderMouse)
        factor = math.pow(1.001, event.angleDelta().y())
        self.grview.scale(factor, 1)

    def zoom_time(self,value):
        self.draw_timeline(self,value)



    def build_interface(self):
        vbox = QtWidgets.QVBoxLayout(self)
        self.grview = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene()
        self.grview.setScene(self.scene)
        self.grview.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.grview.setRenderHint(QtGui.QPainter.Antialiasing)
        self.grview.wheelEvent = lambda event: self.zoom_view_mouse(event)
        self.grview.scale(1, 1)
        vbox.addWidget(self.grview)
        self.draw_timeline()
        self.grview.fitInView(self.grview.sceneRect(), QtCore.Qt.KeepAspectRatio)
        def add_button(text, slot):
            """adds a button to the hbox and connects the slot"""
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(slot)
            vbox.addWidget(button)
        add_button('Mise à jour', lambda: self.draw_timeline())
        label_4 = QtWidgets.QLabel()
        label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        label_4.setObjectName("label_4")

    def draw_timeline(self):
        self.scene.clear()
        timeline_group = QtWidgets.QGraphicsItemGroup()
        self.scene.addItem(timeline_group)
        timeline_group.setZValue(0)
        pen = QtGui.QPen(QtCore.Qt.transparent)
        pen_grey = QtGui.QPen(QtCore.Qt.gray)
        width = 60
        i = 0
        t_0 = self.action[0].time
        t_f = self.action[-1].time
        inter= (t_f - t_0)/2000
        dict={}
        for point in self.action:
            if self.selec[point.action] == 'selected':
                if point.action not in dict:
                    dict[point.action] = i
                    brush = QtGui.QBrush(QtGui.QColor(self.color_form[point.action][0]))
                    y = 100 * dict[point.action]
                    xys = ((point.time - t_0) / inter), y
                    line = QtWidgets.QGraphicsRectItem(xy_line(xys, inter),timeline_group)
                    label = QtWidgets.QLabel(point.action)
                    label_2 = QtWidgets.QLabel(point.action)
                    label.setGeometry(-300,100 * i,250,15)
                    self.scene.addWidget(label)
                    label_2.setGeometry(inter * 8, 100 * i, 250, 15)
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
                item.setPen(pen)
                line.setPen(pen_grey)
                item.setBrush(brush)
                item.setToolTip(point.action+' '+ point.arg)


def xy_coords(xy, width):
    dw = width / 3
    return QtCore.QRectF(xy[0] - dw, xy[1]-dw/3, width/3, width/3)




def xy_line(xy, inter):
    return QtCore.QRectF(-50 , xy[1], (inter*8)+50, 1)