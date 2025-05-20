from martypy import Marty

martin = Marty("wifi","192.168.0.102")

#Fonction pour tourner à 90 selon le côté choisi (gauche/droite)
def turn(side):
    length_step = 8
    step_speed = 1500
    angle = 20

    if side == "left":
        martin.walk(1, "right", -angle, length_step, step_speed)
        martin.walk(1, "left", -angle, length_step, step_speed)
    elif side == "right":
        martin.walk(1, "left", -angle, length_step, step_speed)
        martin.walk(1, "right", -angle, length_step, step_speed)

    martin.stand_straight()


#Se met tout droit
martin.get_ready()

length_step = 8;
step_speed = 1500;
angle = 20

#tourne vers 90° environ pour le nombre de pas i
for i in range (0,5):
    martin.walk(1,"left", -angle, length_step,step_speed)
    martin.walk(1,"right", -angle, length_step,step_speed)

martin.close()

