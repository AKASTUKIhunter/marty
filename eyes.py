from martypy import Marty

#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'
def moveEyes(mood):
    marty = Marty("wifi", "192.168.0.102")
    try:

        marty.eyes(mood,1000)
    except:
        raise "no"

#Changement des yeux en fonction de la mood choisie
