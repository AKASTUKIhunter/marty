from martypy import Marty
from martypy import MartyConnectException

#Fonction pour traverser des cases en marchant
def WalkCase(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.walk(12, 'auto', 0,15,1500,None)

def MoonwalkCase(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.walk(12, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.sidestep('left', 5, 35, 1000)

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(self,nb_cases):
    self.get_ready()
    for i in range(nb_cases):
        self.sidestep('right', 5, 35, 1000)



# Fonction qui lit et exécute les fichiers .dance en absolue
def lecture_dance_abs(self1,name):
    name_file = name + ".dance"
    pos=[1,1]
    with open(name_file, "r", encoding="utf-8") as file:
        type=file.readline()
        
        print("type de fichier :",type)
        taille_grille=int(type[-2])
        pos=[round(taille_grille/2)-1,round(taille_grille/2)-1]  #la position de départ étant le centre de la grille 
        for line in file:
            dest =line
            #On calcul le décalage entre la position actuelle et la destination 
            x=int(dest[0])-pos[0]
            y=int(dest[1])-pos[1]


            print("positions future ",pos,"x: ",x," y=",y)
            
            if((pos[0]+x)>=taille_grille or (pos[0]+x)<taille_grille):
                print("mouvement impossible !!!!")
            else:
                
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

 # Fonction qui lit et exécute les fichiers .dance en séquentiel
    def lecture_dance_seq(self,name):
        name_file = name + ".dance"
        with open(name_file, "r", encoding="utf-8") as file:
            type=file.readline()
            print("type de fichier :",type[:3])
            taille_grille=int(type[-2])
            pos=[round(taille_grille/2)-1,round(taille_grille/2)-1]
            
            
            for line in file:
                direction = ""
                for e in line:
                    if e.isdigit():
                        nb_cases = 0
                        nb_cases += int(e)
                    else:
                        direction = e
                        break

                if direction == "L":
                    SideStepCaseG(self,nb_cases)
                elif direction == "R":
                    SideStepCaseD(self,nb_cases)
                elif direction == "B":  
                    MoonwalkCase(self,nb_cases)
                else:
                    WalkCase(self,nb_cases)


# Fonction qui lit et exécute les fichiers .dance
def lecture_dance(self1,name):
    name_file = name + ".dance"
    with open(name_file, "r", encoding="utf-8") as file:
        type=file.readline()
        print("type de fichier :",type[:3])
        taille_grille=int(type[-2])
        pos=[round(taille_grille/2)-1,round(taille_grille/2)-1]
        print (pos) #la position de départ étant le centre de la grille 
        
        
        if(type[:3]=="SEQ"):
            lecture_dance_seq(self1,name)
        
        elif (type[:3]=="ABS"):
            lecture_dance_abs(self1,name)
        
        
ip="192.168.0.100"
mon_marti = Marty("wifi",ip)

lecture_dance(mon_marti,"cirle")