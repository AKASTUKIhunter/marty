from martypy import Marty
from couleure import get_couleur

#Connexion
Marti = Marty("wifi","192.168.0.103")
Marti.stand_straight()

#Récupère les données du color sensor
color=Marti.get_ground_sensor_reading('LeftColorSensor')
print(color)

#Récupère les données du capteur IR
IR=Marti.get_ground_sensor_reading('RightIRFoot')
print(IR)

#get_couleur à récupérer chez Christ
if get_couleur(color,IR) == "rose":
    Marti.dance()
else:
    Marti.stop()
    Marti.stand_straight()
    print('erreur')



Marti.close()


