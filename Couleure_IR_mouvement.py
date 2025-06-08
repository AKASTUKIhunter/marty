from martypy import Marty

Marti = Marty("wifi","192.168.0.103")
Marti.stand_straight()

''' Dictionnaire de calibration en fonction des couleures et des infrarouges '''
calibration={
    "vert":[26,170],
    "rose":[75,177],
    "bleu":[40,179],
    "rouge":[65,173],
    "bleu_f":[18,159],
    "jaune":[149,180],
    "noir":[13,31],
    "sol":[80,98],
}

# on met une marge pour prendre en compte les différences de lumiètres et les possibles variations au niveau du capteur
marge=6


#On vérifie pour chaque couple couleure, IR si les valeures correspondent à celle d'une couleure calibré
def get_couleur(color,IR):
    c="vert"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="rose"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="bleu"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="rouge"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="bleu_f"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="jaune"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    c="noir"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c
    
    c="sol"
    if ((color<=calibration[c][0]+marge and color>=calibration[c][0]-marge) and (IR<=calibration[c][1]+marge and IR>=calibration[c][1]-marge)):
        return c

#on récupère la couleure 
color=Marti.get_ground_sensor_reading('LeftColorSensor')
print("Capteur couleure :",color)

#on récupère les IR 
IR=Marti.get_ground_sensor_reading('RightIRFoot')
print("Capteur IfraRouge :",IR)
    
Marti.close()