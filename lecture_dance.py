
'''SEQ 3
1L
1U
2R
2B
1L
1U
1B
2U
1L
2R
1L
2B
1U'''

from martypy import Marty

marty= Marty("wifi","192.168.0.103")

case =2
length_step=8
step_speed=1500


#Fonction pour tourner à 90 selon le côté choisi (gauche/droite)
def turn(side):
    length_step = 8
    step_speed = 1500
    angle = 20
    
    marty.stand_straight()
    if side == "left":
        for i in range (0,2):
            marty.walk(1,"right", -angle, length_step,step_speed)
            marty.walk(1,"left", -angle, length_step,step_speed)
    elif side == "right":
        for i in range (0,2):
            marty.walk(1,"left", -angle, length_step,step_speed)
            marty.walk(1,"right", -angle, length_step,step_speed)

    marty.stand_straight()




def lecture_dance():
    with open("file.dance", "r", encoding="utf-8") as file:
        for line in file:
            case=0
            direction =""
            for e in line:
                if e.isdigit():
                    nb_pas+=int(e)
                else:
                    direction=e
                    break
            
            if direction=="L":
                turn("left")
            elif direction=="R":
                turn("right")
            elif direction=="B": #2 fois à gauche pour le retourner à 180°
                turn("left")
                turn("left")
            else:
                marty.stand_straight()
                
            marty.walk(nb_pas*case,"auto", 0, length_step,step_speed)
        
        
            
            
            