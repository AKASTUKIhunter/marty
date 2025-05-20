from martypy import Marty

martin = Marty("wifi","192.168.0.102")

#Se met tout droit
martin.get_ready()

length_step = 1
step_speed = 1000
angle = 10

#Pour le nombre de pas i,
for i in range (0,5):
    martin.stand_straight()
    martin.walk(1,"left", angle, length_step,step_speed)
    martin.stand_straight()
    martin.walk(1,"right", -angle, length_step,step_speed)


martin.stand_straight()

martin.close()