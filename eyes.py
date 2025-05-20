from martypy import Marty

marty = Marty("wifi", "192.168.0.103")

#la string mood peut avoir 5 valeurs:
#'angry','excited','wiggle','normal','wide'

def moveEyes(mood):
    marty.eyes(mood,1000)

#Changement des yeux en fonction de la mood choisie
while(True):
    command = input("Entre le move des yeux \n")

    if command == "wiggle":
        marty.eyes('wiggle', 1000)

    elif command == "excited":
        marty.eyes('excited', 1000)

    elif command == "wide":
        marty.eyes('wide', 1000)

    elif command == "normal":
        marty.eyes('normal', 1000)

    elif command == "angry":
        marty.eyes('angry', 1000)

    elif command == "exit":
        break



marty.close()
