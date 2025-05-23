from martypy import Marty

#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'
def moveEyes(mood,marty):
    try:
        marty.eyes(mood,1000)
    except:
        raise "no"

#Changement des yeux en fonction de la mood choisie
