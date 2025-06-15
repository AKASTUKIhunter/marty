from martypy import Marty



#Fonction pour tourner à 90 selon le côté choisi (gauche/droite)
def turn(marty,side):
    length_step = 8
    step_speed = 1500
    angle = 20

    if side == "left":
        marty.walk(1, "right", -angle, length_step, step_speed)
        marty.walk(1, "left", -angle, length_step, step_speed)
    elif side == "right":
        marty.walk(1, "left", -angle, length_step, step_speed)
        marty.walk(1, "right", -angle, length_step, step_speed)

    marty.stand_straight()


#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'
#Fonction pour bouger les yeux selon la mood
def moveEyes(marty,mood):
    marty.eyes(mood,1000)

#Fonction moonwalk, prends en paramètre un nombre de pas à faire en moonwalk
def walk_backwards(marty,number_of_steps):
    step_speed = 1000
    length_step = 15
    for i in range(0,number_of_steps):
        marty.walk(1, "left", 0, -length_step, step_speed)
        marty.walk(1, "right", 0, -length_step, step_speed)
    marty.stand_straight()


#Fonction pour bouger les bras selon l'angle choisi
#Les variables input1_bras_gauche, input2_bras_droit prennent des int de -100 à 100
def moveArms(marty,input1_bras_gauche, input2_bras_droit):
    marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)

# Fonction qui test si marty est sur le sol ou non
def sensing_test(marty):
        if marty.foot_on_ground('RightIRFoot'):
            marty.dance()
            print("Marti est sur le sol")
        else:
            print("Marti n'est pas sur le sol")

# Fonction de détection d'obstacle
def detect_obs(marty):
        if marty.foot_obstacle_sensed('RightIRFoot'):
            print("Ya un obstacle")
        else:
            print("Marti est safe")
            marty.eyes("wiggle", 1000)

#Salue à Gauche
def waveLeft(marty):
    moveArms(100,0)
    moveArms(50,0)

#Salue à Droite
def waveRight(marty):
    moveArms(0,100)
    moveArms(0,50)

#Kick Left
def kickLeft(marty):
    marty.kick('left',0,2000,None)

#Kick Right
def kickRight(marty):
    marty.kick('right',0,2000,None)

# Fonction de récupération du niveau de batterie
def get_battery(marty):
    status = marty.get_power_status()
    battery_remaining = status['battRemainCapacityPercent']
    print("Batterie restante: ", battery_remaining, "%")


#Fonction pour traverser des cases en marchant
def WalkCase(marty,nb_cases):
    marty.get_ready()
    for i in range(0,nb_cases):
        marty.walk(12, 'auto', 0,15,1500,None)
    marty.stand_straight()

#Focntion pour traverser des cases en reculant
def MoonwalkCase(marty,nb_cases):
    marty.get_ready()
    for i in range(0,nb_cases):
        marty.walk(12, 'auto', 0,-15,1500,None)

#Fonction pour traverser des cases en sidestep gauche
def SideStepCaseG(marty,nb_cases):
    marty.get_ready()
    for i in range(0,nb_cases):
        marty.sidestep('left', 6, 35, 1000)
        marty.stand_straight()

#Fonction pour traverser des cases en sidestep droit
def SideStepCaseD(marty,nb_cases):
    marty.get_ready()
    for i in range(0,nb_cases):
        marty.sidestep('right', 6, 35, 1000)
        marty.stand_straight()
