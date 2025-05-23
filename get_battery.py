from martypy import Marty

#Fonction de récupération du niveau de batterie
def get_battery(marty):
    status = marty.get_power_status()
    battery_remaining = status['battRemainCapacityPercent']
    print("Batterie restante: ", battery_remaining, "%")

#Exemple de code
marty = Marty("wifi","192.168.1.6")

marty.get_ready()
get_battery(marty)

marty.close()