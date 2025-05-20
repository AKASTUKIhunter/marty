from martypy import Marty

martin = Marty("wifi","192.168.0.103")

#Se met tout droit
martin.get_ready()


#Traverse un papier de couleur
#martin.walk(10,'auto',0,15,1500,None)

martin.walk(1,"left",20,30,2000,None)

martin.walk(1,'right',10,30,1500,None)


martin.close()