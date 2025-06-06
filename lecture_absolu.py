from martypy import Marty
from martypy import MartyConnectException

#Fonction pour traverser des cases en marchant
def WalkCase(self,nb_cases):
    self.get_ready()
    for i in range(0,nb_cases):
        self.walk(10, 'auto', 0,15,1500,None)

def MoonwalkCase(self,nb_cases):
    self.get_ready()
    for i in range(0,nb_cases):
        self.walk(10, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(self,nb_cases):
    self.get_ready()
    for i in range(0,nb_cases):
        self.sidestep('left', 5, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(self,nb_cases):
    self.get_ready()
    for i in range(0,nb_cases):
        self.sidestep('right', 5, 35, 1000)





# Fonction qui lit et exécute les fichiers .dance
def lecture_dance_abs(self1,name):
    name_file = name + ".dance"
    pos=[1,1]
    with open(name_file, "r", encoding="utf-8") as file:
        type=file.readline()
        
        print("type :",type)
        for line in file:
            dest =line
            x=int(dest[0])-pos[0]
            y=int(dest[1])-pos[1]


            print(pos,"x: ",x," y=",y)
            if(x<0):
                SideStepCaseG(self1,-x)
            elif(x>0):
                SideStepCaseD(self1,x)
            pos[0]=pos[0]+x
            
            
            if(y<0):
                WalkCase(self1,-y)
            elif (y>0):
                MoonwalkCase(self1,y)
            pos[1]+=y
            
            print(pos)

ip="192.168.0.103"
mon_marti = Marty("wifi",ip)
lecture_dance_abs(mon_marti,"cirle")