from martypy import Marty
from connect import MartyConnection



marty_connec = MartyConnection("192.168.0.103")

#Fonction pour traverser des cases en marchant
def WalkCase(marty_connec,nb_cases):
    marty_connec.marty.get_ready()
    for i in range(1,nb_cases):
        marty_connec.marty.walk(10, 'auto', 0,15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(marty_connec,nb_cases):
    marty_connec.marty.get_ready()
    for i in range(1,nb_cases):
        marty_connec.marty.sidestep('left', 5, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(marty_connec,nb_cases):
    marty_connec.marty.get_ready()
    for i in range(1,nb_cases):
        marty_connec.marty.sidestep('right', 5, 35, 1000)