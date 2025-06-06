from martypy import Marty
from connect import MartyConnection



self= MartyConnection("192.168.0.103")

#Fonction pour traverser des cases en marchant
def WalkCase(self,nb_cases):
    self.marty.get_ready()
    for i in range(1,nb_cases):
        self.marty.walk(10, 'auto', 0,15,1500,None)

def MoonwalkCase(self,nb_cases):
    self.marty.get_ready()
    for i in range(1,nb_cases):
        self.marty.walk(10, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(self,nb_cases):
    self.marty.get_ready()
    for i in range(1,nb_cases):
        self.marty.sidestep('left', 5, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(self,nb_cases):
    self.marty.get_ready()
    for i in range(1,nb_cases):
        self.marty.sidestep('right', 5, 35, 1000)