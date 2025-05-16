from martypy import Marty;

martin = Marty("wifi","192.168.0.104")


martin.stand_straight()
#martin.arms(90,90,1000)
#martin.eyes('angry',1000)

'''nb_pas = 2
pas_demande = 3
if nb_pas<pas_demande:
    martin.walk(1)
    martin.stop()
'''
#Traverse un papier de couleur
martin.walk(10,'auto',0,15,1500,None)
