from martypy import Marty



marty = Marty("wifi","192.168.0.102")

#Fonction moonwalk, prends en paramètre un nombre de pas à faire en moonwalk
def walk_backwards(number_of_steps):
    step_speed = 1000
    length_step = 15
    for i in range(0,number_of_steps):
        marty.walk(1, "left", 0, -length_step, step_speed)
        marty.walk(1, "right", 0, -length_step, step_speed)

    marty.stand_straight()


#Exemple de code test
#Se met tout droit
marty.get_ready()

#Constantes pour la marche de Marty
length_step = 15
step_speed = 1000
angle = 10

#Pour le nombre de pas i, marche en arrière
for i in range (0,5):

    marty.walk(1,"left",0, -length_step, step_speed)
    marty.walk(1,"right", 0, -length_step, step_speed)


marty.stand_straight()

marty.close()