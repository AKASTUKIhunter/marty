from martypy import Marty

Marti = Marty("wifi","192.168.0.104")
Marti.stand_straight()
print(Marti.get_distance_sensor())
'''if Marti.foot_on_ground('RightIRFoot'):
    Marti.dance()
    print("Marti est sur le sol")
else:
    print("Marti n'est pas sur le sol")
'''

if Marti.foot_obstacle_sensed('RightIRFoot'):
    print("Ya un obstacle")


else:
    print("Marti est safe")
    #Marti.eyes("Happy",1000)
Marti.close()