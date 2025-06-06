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



 # Fonction qui lit et exécute les fichiers .dance
    def lecture_dance(self,name):
        name_file = name + ".dance"
        with open(name_file, "r", encoding="utf-8") as file:
            for line in file:
                direction = ""
                for e in line:
                    if e.isdigit():
                        nb_cases = 0
                        nb_cases += int(e)
                    else:
                        direction = e
                        break
                print("nombre de pas: ", nb_cases, " Direction du robot :", direction)

                if direction == "L":
                    SideStepCaseG(self,nb_cases)
                elif direction == "R":
                    SideStepCaseD(self,nb_cases)
                elif direction == "B":  
                    MoonwalkCase(self,nb_cases)
                else:
                    WalkCase(self,nb_cases)
                    
