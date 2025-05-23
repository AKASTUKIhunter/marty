def turn(side, marty):
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
def moveEyes(mood, marty):
    marty.eyes(mood,1000)

#Fonction moonwalk, prends en paramètre un nombre de pas à faire en moonwalk
def walk_backwards(number_of_steps, marty):
    step_speed = 1000
    length_step = 15
    for i in range(0,number_of_steps):
        marty.walk(1, "left", 0, -length_step, step_speed)
        marty.walk(1, "right", 0, -length_step, step_speed)
    marty.stand_straight()


#Fonction pour bouger les bras selon l'angle choisi
#Les variables input1_bras_gauche, input2_bras_droit prennent des int de -100 à 100
def moveArms(input1_bras_gauche, input2_bras_droit, marty):
    marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)

def walk(number_of_steps, marty):
    step_speed = 1000
    length_step = 15
    for i in range(0,number_of_steps):
        marty.walk(1, "left", 0, length_step, step_speed)
        marty.walk(1, "right", 0, length_step, step_speed)
    marty.stand_straight()