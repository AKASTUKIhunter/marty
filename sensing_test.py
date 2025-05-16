from martypy import Marty

Marti = Marty("wifi","192.168.0.104")
Marti.stand_straight()

if Marti.foot_on_ground('RightIRFoot'):
    Marti.dance()
    print("Marti est sur le sol")
else:
    print("Marti n'est pas sur le sol")

Marti.close()