from martypy import Marty
from connect import MartyConnection

marty_connec = MartyConnection("192.168.0.103")

#Fonction pour traverser des cases en marchant
def WalkCase(marty_connec,nb_cases):
    marty_connec.marty.get_ready()
    for i in range(1,nb_cases):
        marty_connec.marty.walk(10, 'auto', 0,15,1500,None)

#Fonction pour traverser des cases en sidestep
def SideStepCase(marty_connec,nb_cases):
    marty_connec.marty.get_ready()
    for i in range(1,nb_cases):
        marty_connec.marty.sidestep() #Paramètres à ajouter après les mesures

