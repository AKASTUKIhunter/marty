from martypy import Marty
from connect import MartyConnection

martin = MartyConnection("192.168.0.102")

#Se met tout droit
martin.marty.get_ready()




#Traverse un papier de couleur en marchant
martin.walk(10,'auto',0,15,1500,None)
#Traverse un papier de couleur en sidestep
martin.sidestep('')

#Dance !
martin.dance()



martin.close()