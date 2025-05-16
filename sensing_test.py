import martypy

Marti = Marty("wifi","192.168.0.104")

if Marti.foot_on_ground(nomcapteur):
    Marti.walk(3)
elif Marti.foot_obstacle_sensed(nomcapteur):
    Marti.stop()