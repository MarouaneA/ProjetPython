
class Point(object):

    def __init__(self,time,action,arg):
        self.time=time
        self.action=action
        self.arg=arg
    def __repr__(self):
        return "{0.action}".format(self)

def load_actions(fichier):
    ''' liste des Points du fichier 'fichier' , et la liste des actions différentes du fichier '''
    liste_points = []
    with open(fichier,'r') as f:
        for line in f:
            l=str.split(line)
            L= l[0].split(',')
            liste_points.append(Point(int(L[0]),L[2]," , ".join(L[3:])))

    liste_act_diff = []
    for point in liste_points:
        if point.action not in liste_act_diff:
            liste_act_diff.append(point.action)
    return liste_points, liste_act_diff

