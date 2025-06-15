from martypy import Marty
import json
from martypy import MartyConnectException
from colorDetection import get_color
from feelScraper import FeelScraper
from useController import ControllerControl
from useKeyboard import KeyboardControl
from PyQt6.QtWidgets import QPushButton
import os

class MartyConnection:
    def __init__(self):
        self.ip: str
        self.controller: ControllerControl
        self.keyboard: KeyboardControl
        self.color: str
        self.speed: int
        self.calibration = self.readCalibrationFromFile()
        self.feelScraper = FeelScraper(self.calibration)

        self.case: int  # le nombre de pas nécéssaire pour une case

    def connect(self, ip: str):
        try:
            self.marty = Marty("wifi", ip)
            self.ip = ip
            print(f"Connected to Marty at {ip}")
            self.marty.get_ready()
            self.controller = ControllerControl(self)
            self.keyboard = KeyboardControl(self)
            return self.marty

        except MartyConnectException as e:
            print(f"Error while connecting to Marty at {ip}: {e}")
        except Exception as e:
            print(f"Unexpected error while connecting to Marty at {ip}: {e}")
    
    def feel(self):
        try:
            color = self.marty.get_ground_sensor_reading('LeftColorSensor')

            #Récupère les données du capteur IR
            ir = self.marty.get_ground_sensor_reading('RightIRFoot')

            detected_color = get_color(color, ir, self.calibration)
            
            feels = self.feelScraper.feels
            
            print(color, ir, detected_color, feels)
            if detected_color in feels.keys():
                mood = feels[detected_color]['mood']
                print(feels[detected_color])
                self.moveEyes(mood)
                self.marty.disco_color(feels[detected_color]['color'], self.marty.Disco.EYES, api="led")
            
        except Exception as e:
            print(f"Error while feeling: {e}")

    def calibrateColors(self, button: QPushButton):
        if hasattr(self, 'marty'):
            colors = ["red", "green", "blue", "yellow", "purple", "black", "pink"]
            # Use self.calibration to persist calibration data
            calibration = self.calibration

            # Disconnect previous connections to avoid multiple triggers
            try:
                button.clicked.disconnect()
            except Exception:
                print("No previous connection to disconnect")

            if button.text() == "Calibration" or button.text() == "Calibrate colors again":
                button.setText("Calibrate {}".format(colors[0]))
                button.clicked.connect(lambda: self.changeButton(colors[0], calibration, button)) # type: ignore
            elif (button.text().startswith("Calibrate ") and
                button.text().split(" ")[1].lower() in colors and colors.index(button.text().split(" ")[1].lower()) < len(colors) - 1):
                current_color = button.text().split(" ")[1].lower()
                button.setText("Calibrate {}".format(colors[colors.index(current_color) + 1]))
                button.clicked.connect(lambda: self.changeButton(colors[colors.index(current_color) + 1], calibration, button)) # type: ignore
            elif button.text() == "Calibrate {}".format(colors[-1]):
                self.saveCalibrationToFile()
                button.setText("Calibrate colors again")
                button.clicked.connect(lambda: self.calibrateColors(button))
        else:
            print("Marty is not connected. Cannot calibrate colors.")

    def saveCalibrationToFile(self, filename: str = "calibration.json"):
        with open(filename, 'w') as file:
            json.dump(self.calibration, file, indent=4)
        print(f"Calibration saved to {filename}")

    def readCalibrationFromFile(self, filename: str = "calibration.json"):
        try:
            with open(filename, 'r') as file:
                calibration = json.load(file)
                print(f"Calibration : {calibration} loaded from {filename}")
                return calibration
        except FileNotFoundError:
            print(f"Calibration file {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}.")

    def changeButton(self, color: str, calibration: dict, button: QPushButton):
        detected_color = self.marty.get_ground_sensor_reading("LeftColorSensor")
        detected_ir = self.marty.get_ground_sensor_reading("RightIRFoot")
        calibration[color] = [detected_color, detected_ir]
        self.calibration = calibration
        print(self.calibration)
        self.calibrateColors(button)

    # Fonction de détection d'obstacle
    def detect_obs(self):
        try:    
            if self.marty.foot_obstacle_sensed('RightIRFoot'):
                print("Ya un obstacle")
            else:
                print("Marti est safe")
                self.marty.eyes("wiggle", 1000)
        except Exception as e:
            print(f"Error while detecting obstacle: {e}")

    # Kick Left
    def kickLeft(self):
        try:
            self.marty.kick('left', 0, 2000, None)
        except Exception as e:
            print(f"Error while kicking left: {e}")

    # Kick Right
    def kickRight(self):
        try:
            self.marty.kick('right', 0, 2000, None)
        except Exception as e:
            print(f"Error while kicking right: {e}")

    # Fonction de récupération du niveau de batterie
    def get_battery(self):
        try:
            status = self.marty.get_power_status()
            battery_remaining = status['battRemainCapacityPercent']
            print("Batterie restante: ", battery_remaining, "%")
            return battery_remaining
        except Exception as e:
            print(f"Error while getting battery status: {e}")

  #Fonction pour traverser des cases en marchant
    def WalkCase(self,nb_cases):
        try:
            self.marty.get_ready()
            for i in range(0,nb_cases):
                self.marty.walk(12, 'auto', 0,15,1500,None)
                self.marty.stand_straight()
            
            self.feel()
        except Exception as e:
            print(f"Error while walking case: {e}")

    def MoonwalkCase(self,nb_cases):
        try:
            self.marty.get_ready()
            for i in range(0,nb_cases):
                self.marty.walk(12, 'auto', 0,-15,1500,None)
                self.marty.stand_straight()
            
            self.feel()
        except Exception as e:
            print(f"Error while moonwalking case: {e}")

    #Fonction pour traverser des cases en sidestep gauche
    def SideStepCaseG(self,nb_cases):
        try:
            self.marty.get_ready()
            for i in range(0,nb_cases):
                self.marty.sidestep('left', 6, 35, 1000)
                self.marty.stand_straight()
            self.feel()
        except Exception as e:
            print(f"Error while sidestepping left: {e}")

    #Fonction pour traverser des cases en sidestep droit
    def SideStepCaseD(self,nb_cases):
        try:
            self.marty.get_ready()
            for i in range(0,nb_cases):
                self.marty.sidestep('right', 6, 35, 1000)
                self.marty.stand_straight()
            self.feel()
        except Exception as e:
            print(f"Error while sidestepping right: {e}")

    # Fonction qui lit et exécute les fichiers .dance en absolue
    def lecture_dance_abs(self,name):
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

                print("taille grille",taille_grille)
                print("positions future ",pos,"x: ",x," y=",y)
                
                if((pos[0]+x)>=taille_grille or (pos[0]+x)<0):
                    print("mouvement impossible !!!!")
                else:
                    
                    if(x<0):
                        self.SideStepCaseG(-x)
                    elif(x>0):
                        self.SideStepCaseD(x)
                    pos[0]=pos[0]+x
                    
                    
                    if(y<0):
                        self.WalkCase(-y)
                    elif (y>0):
                        self.MoonwalkCase(y)
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
                    self.SideStepCaseG(nb_cases)
                elif direction == "R":
                    self.SideStepCaseD(nb_cases)
                elif direction == "B":  
                    self.MoonwalkCase(nb_cases)
                else:
                    self.WalkCase(nb_cases)

    def writing_file_abs(self, move, filename):
        valid_positions = [(1,1), (1,0), (0,1), (0,0), (2,1), (1,2), (2,0), (0,2), (2,2)]
        
        file_empty = not os.path.exists(filename) or os.path.getsize(filename) == 0
        
        x, y = self.robot_position if hasattr(self, 'robot_position') else (1, 1)
        
        if move == "avancer":
            new_pos = (x, y-1)
        elif move == "reculer":
            new_pos = (x, y+1)
        elif move == "droite":
            new_pos = (x+1, y)
        elif move == "gauche":
            new_pos = (x-1, y)
        else:
            raise ValueError("Mouvement invalide. Utilisez 'avancer', 'reculer', 'droite' ou 'gauche'.")
        
        # Si la nouvelle position n'est pas valide, ne rien faire (retourner immédiatement)
        if new_pos not in valid_positions:
            return
        
        # Mettre à jour la position du robot
        self.robot_position = list(new_pos)
        
        # Écrire dans le fichier
        with open(filename, "a") as script:
            if file_empty:
                script.write("ABS 3\n")
            script.write(f"{new_pos[0]}{new_pos[1]}\n")

    # Fonction qui lit et exécute les fichiers .dance
    def lecture_dance(self,name):
        try:
            name_file = name + ".dance"
            with open(name_file, "r", encoding="utf-8") as file:
                type=file.readline()
                print("type de fichier :",type[:3])
                taille_grille=int(type[-2])
                pos=[round(taille_grille/2)-1,round(taille_grille/2)-1]
                print (pos) #la position de départ étant le centre de la grille 
                
                
                if(type[:3]=="SEQ"):
                    self.lecture_dance_seq(name)
                
                elif (type[:3]=="ABS"):
                    self.lecture_dance_abs(name)
        except FileNotFoundError:
            print(f"Erreur lors de la lecture: Le fichier {name_file} n'existe pas.")
    
    def Addline(self, move, filename):
        file_empty = not os.path.exists(filename) or os.path.getsize(filename) == 0

        with open(filename, "a") as script:
            if file_empty:
                script.write("SEQ 3\n")
            script.write(move + "\n")

    def disconnect(self):
        if hasattr(self, 'marty'):
            self.marty.close()
            print("Disconnected from Marty")
        else:
            print("No Marty connection to disconnect")

    def turn(self, side: str):
        try:
            length_step = 8
            step_speed = 1500
            angle = 20

            if side == "left":
                self.marty.walk(1, "right", angle, length_step, step_speed)
                self.marty.walk(1, "left", angle, length_step, step_speed)
            elif side == "right":
                self.marty.walk(1, "left", -angle, length_step, step_speed)
                self.marty.walk(1, "right", -angle, length_step, step_speed)

            self.marty.stand_straight()
        except Exception as e:
            print(f"Error in turn function: {e}")
    
    def get_ready(self):
        try:
            self.marty.get_ready()
        except Exception as e:
            print(f"Error in get_ready function: {e}")

    def dance(self):
        try:
            self.marty.dance()
        except Exception as e:
            print(f"Error in dance function: {e}")

    def celebrate(self):
        try:
            self.marty.celebrate()
        except Exception as e:
            print(f"Error in celebrate function: {e}")

    def moveEyes(self, mood: str):
        try:
            self.marty.eyes(mood, 1000)
        except Exception as e:
            print(f"Error in moveEyes function: {e}")

    def waveRightHand(self, input1_bras_gauche: int, input2_bras_droit: int):
        try:
            self.marty.arms(input1_bras_gauche, -abs(input2_bras_droit),1000,None)
            self.marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
            self.marty.arms(input1_bras_gauche, -abs(input2_bras_droit),1000,None)
            self.marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
            self.marty.arms(0, 0,1000,None)
        except Exception as e:
            print(f"Error in waveRightHand function: {e}")

    def waveLeftHand(self, input1_bras_gauche: int, input2_bras_droit: int):
        try:
            self.marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
            self.marty.arms(-abs(input1_bras_gauche), input2_bras_droit,1000,None)
            self.marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
            self.marty.arms(-abs(input1_bras_gauche), input2_bras_droit,1000,None)
            self.marty.arms(0, 0,1000,None)
        except Exception as e:
            print(f"Error in waveLeftHand function: {e}")