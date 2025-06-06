
'''ABS 5
22
02
42
24
44
04
00
40
31
22
13
23
22'''

from martypy import Marty
from connect import MartyConnection

marty= Marty("wifi","192.168.0.103")



def lecture_dance_abs():
    pos=[1,1]
    with open("dominance.dance", "r", encoding="utf-8") as file:
        for line in file:
            e=int(line)
            
            x=e[0]
            y=e[1] 
            
            if(x<pos[0]):
                nb_pas 
            print("nombre de pas: ",nb_pas," Direction du robot :",direction)
            
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
        
        
            