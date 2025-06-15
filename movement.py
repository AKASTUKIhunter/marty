from martypy import Marty

def turn(side: str, marty: Marty):
    try:
        length_step = 8
        step_speed = 1500
        angle = 20

        if side == "left":
            marty.walk(1, "right", angle, length_step, step_speed)
            marty.walk(1, "left", angle, length_step, step_speed)
        elif side == "right":
            marty.walk(1, "left", -angle, length_step, step_speed)
            marty.walk(1, "right", -angle, length_step, step_speed)

        marty.stand_straight()
    except Exception as e:
        print(f"Error in turn function: {e}")

#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'
#Fonction pour bouger les yeux selon la mood
def moveEyes(mood: str, marty: Marty):
    try:
        marty.eyes(mood, 1000)
    except Exception as e:
        print(f"Error in moveEyes function: {e}")

#Fonction moonwalk, prends en paramètre un nombre de pas à faire en moonwalk
def walk_backwards(number_of_steps: int, marty: Marty):
    try:
        step_speed = 1000
        length_step = 15
        for i in range(0,number_of_steps):
            marty.walk(1, "left", 0, -length_step, step_speed)
            marty.walk(1, "right", 0, -length_step, step_speed)
        marty.stand_straight()
    except Exception as e:
        print(f"Error in walk_backwards function: {e}")


#Fonction pour bouger les bras selon l'angle choisi
#Les variables input1_bras_gauche, input2_bras_droit prennent des int de -100 à 100
def moveArms(input1_bras_gauche: int, input2_bras_droit: int, marty: Marty):
    try:
        marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
    except Exception as e:
        print(f"Error in moveArms function: {e}")

def waveRightHand(input1_bras_gauche: int, input2_bras_droit: int, marty: Marty):
    try:
        marty.arms(input1_bras_gauche, -abs(input2_bras_droit),1000,None)
        marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
        marty.arms(input1_bras_gauche, -abs(input2_bras_droit),1000,None)
        marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
        marty.arms(0, 0,1000,None)
    except Exception as e:
        print(f"Error in waveRightHand function: {e}")

def waveLeftHand(input1_bras_gauche: int, input2_bras_droit: int, marty: Marty):
    try:
        marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
        marty.arms(-abs(input1_bras_gauche), input2_bras_droit,1000,None)
        marty.arms(input1_bras_gauche, input2_bras_droit,1000,None)
        marty.arms(-abs(input1_bras_gauche), input2_bras_droit,1000,None)
        marty.arms(0, 0,1000,None)
    except Exception as e:
        print(f"Error in waveLeftHand function: {e}")

def walk(number_of_steps: int, marty: Marty):
    try:
        step_speed = 1000
        length_step = 15
        for i in range(0,number_of_steps):
            marty.walk(1, "left", 0, length_step, step_speed)
            marty.walk(1, "right", 0, length_step, step_speed)
        marty.stand_straight()
    except Exception as e:
        print(f"Error in walk function: {e}")


# Kick left
def kickLeft(marty: Marty):
    try:
        marty.kick('left',0,2000,None)
    except Exception as e:
        print(f"Error in kickLeft function: {e}")

# Kick Right
def kickRight(marty: Marty):
    try:
        marty.kick('right',0,2000,None)
    except Exception as e:
        print(f"Error in kickRight function: {e}")

def dance(marty: Marty):
    try:
        marty.dance()
    except Exception as e:
        print(f"Error in dance function: {e}")

def get_ready(marty: Marty):
    try:
        marty.get_ready()
    except Exception as e:
        print(f"Error in get_ready function: {e}")

def celebrate(marty: Marty):
    try:
        marty.celebrate()
    except Exception as e:
        print(f"Error in celebrate function: {e}")