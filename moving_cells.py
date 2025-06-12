from martypy import Marty
from connect import MartyConnection

marty_connec = Marty("wifi","192.168.0.100")

#Fonction pour traverser des cases en marchant
def WalkCase(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.walk(12, 'auto', 0,15,1500,None)
    marty.stand_straight()

def MoonwalkCase(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.walk(12, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.sidestep('left', 5, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.sidestep('right', 5, 35, 1000)
    marty.stand_straight()



MoonwalkCase(marty_connec,1)
SideStepCaseG(marty_connec,1)
SideStepCaseD(marty_connec,2)
WalkCase(marty_connec,2)


marty_connec.close()
