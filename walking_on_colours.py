from martypy import Marty

Marti = Marty("wifi","192.168.0.104")
Marti.stand_straight()

#while(Marti.get_ground_sensor_reading('LeftColorSensor') = 65):

color=Marti.get_ground_sensor_reading('LeftColorSensor')
print(color)

IR=Marti.get_ground_sensor_reading('RightIRFoot')
print(IR)

if get_couleur(color,IR) == "rose":
    Marti.dance()
else:
    Marti.stop()
    Marti.stand_straight()
    print('erreur')



Marti.close()
#Marti.walk(20,'auto',0,15,1000,None)

