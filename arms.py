from martypy import Marty

marty = Marty("wifi", "192.168.1.6")
marty.stand_straight()

#Salue à Gauche
def waveLeft(marty):
    moveArms(100,0)
    moveArms(50,0)
    moveArms(100, 0)
    moveArms(50, 0)

#Salue à Droite
def waveRight(marty):
    moveArms(0, 100)
    moveArms(0, 50)
    moveArms(0, 100)
    moveArms(0, 50)

#Fonction pour bouger les bras
#Les variables input1_bras_gauche, input2_bras_droit prennent des int de -100 à 100
def moveArms(input1_bras_gauche, input2_bras_droit):
    marty.arms(input1_bras_gauche, input2_bras_droit,400,None)


#Mouvement des bras selon l'input
'''while(True):

    command_bras = int(input("Quel bras ? (left,right,both) \n"))


    command_mouv_BD = int(input("Entrez l'angle du mouv du bras droite(-100 à 100)\n"))


    if command_bras == "left":
        command_mouv_BG = int(input("Entrez l'angle du mouv du bras gauche(-100 à 100)) \n"))
        marty.arms(command_mouv_BG, 0, 1000, None)

    elif command_bras == "right":
        command_mouv_BD = int(input("Entrez l'angle du mouv du bras droite(-100 à 100)\n"))
        marty.arms(0, command_mouv_BD, 1000, None)

    elif command_bras == "both":
        command_mouv_BG = int(input("Entrez l'angle du mouv du bras gauche(-100 à 100)) \n"))
        command_mouv_BD = int(input("Entrez l'angle du mouv du bras droite(-100 à 100)\n"))
        marty.arms(command_mouv_BG, command_mouv_BD, 1000, None)


    elif (command_bras or command_mouv) == "exit":
        break
        marty.close()
'''
#Exemple de Code avec WaveRight et WaveLeft
marty.get_ready()
waveLeft(marty)
waveRight(marty)
marty.close()