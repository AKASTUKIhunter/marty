from martypy import Marty

#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'
def moveEyes(mood: str, marty: Marty):
    try:
        marty.eyes(mood,1000)
    except Exception as e:
        print(f"Error while trying to move eyes : {e}")

#Changement des yeux en fonction de la mood choisie
