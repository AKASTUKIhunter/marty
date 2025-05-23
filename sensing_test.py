from martypy import Marty

#Connexion
marty = Marty("wifi","192.168.1.6")
marty.stand_straight()
print(marty.get_distance_sensor())

#Fonction qui test si marty est sur le sol ou non
def sensing_test(marty):
    if marty.foot_on_ground('RightIRFoot'):
        marty.dance()
        print("Marti est sur le sol")
    else:
        print("Marti n'est pas sur le sol")


#Fonction de détection d'obstacle
def detect_obs(marty):
    if marty.foot_obstacle_sensed('RightIRFoot'):
        print("Ya un obstacle")
    else:
        print("Marti est safe")
        marty.eyes("wiggle", 1000)

detect_obs(marty)
marty.close()