from PyQt5 import QtGui, QtWidgets

X0 = 300
Y0 = 150
SCALE = 0.5

def get_color(n):
    """Renvoie une QColor en fonction de l'entier 'n'"""
    d = (0xff, 0xdd, 0xbb, 0x99, 0x77, 0x55)[(n // 6) % 6]
    r, v, b = ((d,0,0), (0,d,0), (0,0,d), (d,d,0), (d,0,d), (0,d,d))[n % 6]
    return QtGui.QColor(r, v, b)

class Map(object):

    def __init__(self):
        """Cree la zone graphique"""
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QWidget()
        scene = QtWidgets.QGraphicsScene(self.window)
        self.view = QtWidgets.QGraphicsView(scene)
        self.view.resize(2 * X0, 2 * X0)
        self.view.centerOn(float(X0), float(Y0))
        self.view.scale(SCALE, -SCALE)
        self.view.setDragMode(self.view.ScrollHandDrag)
        self.view.wheelEvent = self._rescale
        self.view.keyPressEvent = self._key
        self.flight_items = []
        self.view.show()

    def draw_airports(self, apt_dict):
        """Dessine les aeroports du dictionnaire 'apt_dict'"""
        color = QtGui.QColor('blue')
        scene = self.view.scene()
        for code, apt in apt_dict.items():
            scene.addEllipse(apt.x-4, apt.y-4, 8, 8, color, color)

    def draw_flights(self, flights):
        """Dessine les vols de la liste 'flights'"""
        scene = self.view.scene()
        for item in self.flight_items: scene.removeItem(item)
        self.flight_items = []
        for flight in flights:
            x0, y0 = flight.orig.x, flight.orig.y
            x1, y1 = flight.dest.x, flight.dest.y
            try: color = get_color(flight.colors[0])
            except: color = get_color(0)
            pen = QtGui.QPen(color, 5)
            self.flight_items.append(scene.addLine(x0, y0, x1, y1, pen))

    def show(self):
        self.app.exec_()

    def _rescale(self, event):
        """Roulette souris"""
        self.view.setTransformationAnchor(self.view.AnchorUnderMouse)
        delta = event.angleDelta().y()
        factor = 1.1 if delta > 0 else 1/1.1
        self.view.scale(factor, factor)

    def _key(self, event):
        """ Touche clavier"""
        if event.text() == 'q':
            self.app.quit()
