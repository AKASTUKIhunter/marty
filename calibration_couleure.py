from martypy import Marty

ip="192.168.0.104"
my_marty = Marty("wifi",ip)

color=my_marty.get_ground_sensor_reading('LeftColorSensor')
print(color)

IR=my_marty.get_ground_sensor_reading('RightIRFoot')
print(IR)



my_marty.close()