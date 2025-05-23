from martypy import Marty

marty = Marty("wifi","192.168.0.102")

#Fonction pour tourner à 90 selon le côté choisi (gauche/droite)
def turn(side):
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

#Exemple de code test
#Se met tout droit
marty.get_ready()

length_step = 8;
step_speed = 1500;
angle = 20

#tourne vers 90° environ pour le nombre de pas i
for i in range (0,5):
    marty.walk(1,"left", -angle, length_step,step_speed)
    marty.walk(1,"right", -angle, length_step,step_speed)

marty.close()

