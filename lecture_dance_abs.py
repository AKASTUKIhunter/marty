from martypy import Marty
from martypy import MartyConnectException

#Fonction pour traverser des cases en marchant
def WalkCase(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.walk(10, 'auto', 0,15,1500,None)

def MoonwalkCase(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.walk(10, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.sidestep('left', 6, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.sidestep('right', 6, 35, 1000)





# Fonction qui lit et exécute les fichiers .dance
def lecture_dance_abs(self1,name):
    name_file = name + ".dance"
    pos=[1,1]
    with open(name_file, "r", encoding="utf-8") as file:
        type=file.readline()
        
        print("type de fichier :",type)
        taille_grille=int(type[-2])
        pos=[round(taille_grille/2),round(taille_grille/2)]  #la position de départ étant le centre de la grille 
        for line in file:
            dest =line
            #On calcul le décalage entre la position actuelle et la destination 
            x=int(dest[0])-pos[0]
            y=int(dest[1])-pos[1]


            print("positions future ",pos,"x: ",x," y=",y)
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
            
            print("position actuelle: " ,pos)

ip="192.168.0.103"
mon_marti = Marty("wifi",ip)
lecture_dance_abs(mon_marti,"cirle")