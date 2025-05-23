from martypy import Marty

#Kick Left
def kickLeft(marty):
    marty.kick('left',0,2000,None)

#Kick Right
def kickRight(marty):
    marty.kick('right',0,2000,None)

#Exemple de code
marty = Marty("wifi","192.168.1.6")
marty.get_ready()
kickLeft(marty)
