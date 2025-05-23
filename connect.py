from martypy import Marty
from martypy import MartyConnectException
from useController import ControllerControl
from useKeyboard import KeyboardControl

class MartyConnection:
    def __init__(self):
        self.ip : str
        self.marty: Marty
        self.controller: ControllerControl
        self.keyboard: KeyboardControl
        self.color  : str
        self.speed : int
        
        self.case : int #le nombre de pas nécéssaire pour une case

    def connect(self, ip: str):
        try:
            self.marty = Marty("wifi", ip)
            self.ip = ip
            print(f"Connected to Marty at {ip}")
            self.marty.get_ready()
            self.controller = ControllerControl(self.marty)
            self.keyboard = KeyboardControl(self.marty)
            return self.marty

        except MartyConnectException as e:
            print(f"Error while connecting to Marty at {ip}: {e}")
        except Exception as e:
            print(f"Unexpected error while connecting to Marty at {ip}: {e}")
        
        
        def turn(side):          
            self.stand_straight()
            angle=20
            length_step=8
            step_speed=1500
            
            self.stand_straight()
            if side == "left":
                for i in range(0,2):
                    self.walk(1,"right", -angle, length_step,step_speed)
                    self.walk(1,"left", -angle, length_step,step_speed)
            elif side == "right":
                for i in range(0,2):
                    self.walk(1,"left", -angle, length_step,step_speed)
                    self.walk(1,"right", -angle, length_step,step_speed)
            self.stand_straight()
            
        def walk_backwards(number_of_steps):
            self.speed = 1000
            length_step = 15
            
            self.stand_straight()
            for i in range(0,number_of_steps):
                self.walk(1, "left", 0, -length_step, self.speed)
                self.walk(1, "right", 0, -length_step, self.speed)
            self.stand_straight()
        
        def moveArms(input1_bras_gauche, input2_bras_droit):
            self.arms(input1_bras_gauche, input2_bras_droit,1000,None)
            
        # Fonction de détection d'obstacle
        def detect_obs():
            if self.foot_obstacle_sensed('RightIRFoot'):
                print("Ya un obstacle")
            else:
                print("Marti est safe")
                self.eyes("wiggle", 1000)
        
        #Kick Left
        def kickLeft():
            self.kick('left',0,2000,None)
            
        #Kick Right
        def kickRight():
            self.kick('right',0,2000,None)
            
        # Fonction de récupération du niveau de batterie
        def get_battery():
            status = self.get_power_status()
            battery_remaining = status['battRemainCapacityPercent']
            print("Batterie restante: ", battery_remaining, "%")
            
        # Fonction qui lit et exécute les fichiers .dance
        def lecture_dance(name):
            name_file=name+".dance"
            with open(name_file, "r", encoding="utf-8") as file:
                for line in file:
                    case=0
                    direction =""
                    for e in line:
                        if e.isdigit():
                            nb_pas+=int(e)
                        else:
                            direction=e
                            break  
                    print("nombre de pas: ",nb_pas," Direction du robot :",direction)
                    
                    if direction=="L":
                        turn("left")
                    elif direction=="R":
                        turn("right")
                    elif direction=="B": #2 fois à gauche pour le retourner à 180°
                        turn("left")
                        turn("left")
                    else:
                        self.stand_straight()
                    length_step=10
                    self.walk(nb_pas*self.case,"auto", 0, length_step,self.speed)
                