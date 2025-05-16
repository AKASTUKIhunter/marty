import martypy

Marti = Marty("wifi","192.168.1.1")

if Marti.foot_on_ground(nomcapteur):
    Marti.walk(3)
elif Marti.foot_obstacle_sensed(nomcapteur):
    Marti.stop()