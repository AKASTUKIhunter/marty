from martypy import Marty
import json
from martypy import MartyConnectException
from colorDetection import get_color
import colorDetection
from feelScraper import FeelScraper
from useController import ControllerControl
from useKeyboard import KeyboardControl
from eyes import moveEyes
from PyQt6.QtWidgets import QPushButton

class MartyConnection:
    def __init__(self):
        self.ip: str
        self.marty: Marty
        self.controller: ControllerControl
        self.keyboard: KeyboardControl
        self.color: str
        self.speed: int
        self.feelScraper: FeelScraper
        self.calibration = self.readCalibrationFromFile()

        self.case: int  # le nombre de pas nécéssaire pour une case

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

    def walk(self, number_of_steps: int, marty):
        step_speed = 1000
        length_step = 15
        for i in range(0, number_of_steps):
            marty.walk(1, "left", 0, length_step, step_speed)
            marty.walk(1, "right", 0, length_step, step_speed)
        marty.stand_straight()
        self.feel()

    
    def feel(self):
        color = self.marty.get_ground_sensor_reading('LeftIRFoot')

        #Récupère les données du capteur IR
        ir = self.marty.get_ground_sensor_reading('RightColorSensor')

        detected_color = get_color(color, ir)

        feelscraper = FeelScraper("real.feels")
        
        feels = feelscraper.feels
        
        print(color, ir, detected_color, feels)
        if detected_color in feels:
            mood = feels[color]['mood']
            moveEyes(mood, self.marty)

    def sidestep(self, side):
        self.marty.sidestep(side)
        self.feel()

    def calibrateColors(self, button: QPushButton):
        colors = ["green", "cyan", "red", "blue", "yellow", "purple"]
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

    def turn(self, side):
        self.marty.stand_straight()
        angle = 20
        length_step = 8
        step_speed = 1500

        self.marty.stand_straight()
        if side == "left":
            for i in range(0, 2):
                self.marty.walk(1, "right", -angle, length_step, step_speed)
                self.marty.walk(1, "left", -angle, length_step, step_speed)
        elif side == "right":
            for i in range(0, 2):
                self.marty.walk(1, "left", -angle, length_step, step_speed)
                self.marty.walk(1, "right", -angle, length_step, step_speed)
        self.marty.stand_straight()

    def walk_backwards(self, number_of_steps):
        speed = 1000
        length_step = 15

        self.marty.stand_straight()
        for i in range(0, number_of_steps):
            self.marty.walk(1, "left", 0, -length_step, speed)
            self.marty.walk(1, "right", 0, -length_step, speed)
        self.marty.stand_straight()

    def moveArms(self, input1_bras_gauche, input2_bras_droit):
        self.marty.arms(input1_bras_gauche, input2_bras_droit, 1000, None)

    # Fonction de détection d'obstacle
    def detect_obs(self):
        if self.marty.foot_obstacle_sensed('RightIRFoot'):
            print("Ya un obstacle")
        else:
            print("Marti est safe")
            self.marty.eyes("wiggle", 1000)

    # Kick Left
    def kickLeft(self):
        self.marty.kick('left', 0, 2000, None)

    # Kick Right
    def kickRight(self):
        self.marty.kick('right', 0, 2000, None)

    # Fonction de récupération du niveau de batterie
    def get_battery(self):
        status = self.marty.get_power_status()
        battery_remaining = status['battRemainCapacityPercent']
        print("Batterie restante: ", battery_remaining, "%")

   #Fonction pour traverser des cases en marchant
    def WalkCase(self,nb_cases):
        self.marty.get_ready()
        for i in range(0,nb_cases):
            self.marty.walk(10, 'auto', 0,15,1500,None)

    def MoonwalkCase(self,nb_cases):
        self.marty.get_ready()
        for i in range(0,nb_cases):
            self.marty.walk(10, 'auto', 0,-15,1500,None)

    #Fonction pour traverser des cases en sidestep gauche
    def SideStepCaseG(self,nb_cases):
        self.marty.get_ready()
        for i in range(0,nb_cases):
            self.marty.sidestep('left', 5, 35, 1000)

    #Fonction pour traverser des cases en sidestep droit
    def SideStepCaseD(self,nb_cases):
        self.marty.get_ready()
        for i in range(0,nb_cases):
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
                    elif e=="S" or e==" ":
                        nb_cases = 0
                    else:
                        direction = e
                        break
                print("nombre de pas: ", nb_cases, " Direction du robot :", direction)

                if direction == "L":
                    self.SideStepCaseG(nb_cases)
                elif direction == "R":
                    self.SideStepCaseD(nb_cases)
                elif direction == "B":  
                    self.MoonwalkCase(nb_cases)
                elif direction == "U":
                    self.WalkCase(nb_cases)