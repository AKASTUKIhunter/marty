from martypy import Marty
from connect import MartyConnection

marty_connec = Marty("wifi","192.168.0.100")

#Fonction pour traverser des cases en marchant
def WalkCase(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.walk(12, 'auto', 0,15,1500,None)
    marty.stand_straight()

#Focntion pour traverser des cases en reculant
def MoonwalkCase(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.walk(12, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.sidestep('left', 6, 35, 1000)
        marty.stand_straight()

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(marty,nb_cases):
    marty_connec.get_ready()
    for i in range(0,nb_cases):
        marty_connec.sidestep('right', 6, 35, 1000)
        marty.stand_straight()




#test
SideStepCaseG(marty_connec,2)


marty_connec.close()
