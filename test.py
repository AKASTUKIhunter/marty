from martypy import Marty
from connect import MartyConnection

#martin = MartyConnection("192.168.0.102")

martin = Marty("wifi","192.168.0.103")
#Se met tout droit

martin.get_ready()

#martin.disco_color("blue",martin.Disco.EYES, api='led')



martin.walk(10, 'auto', 0,-15,1500,None)

#martin.get_ready()

#Traverse un papier de couleur en marchant
#martin.walk(10,'auto',0,15,1500,None)
#Traverse un papier de couleur en sidestep
#martin.sidestep('')

#Dance !




martin.close()