from martypy import Marty

martin = Marty("wifi","192.168.0.102")

#Se met tout droit
martin.get_ready()

length_step = 15
step_speed = 1000
angle = 10

#Pour le nombre de pas i, marche arrière
for i in range (0,5):

    martin.walk(1,"left",0, -length_step, step_speed)
    martin.walk(1,"right", 0, -length_step, step_speed)


martin.stand_straight()

martin.close()