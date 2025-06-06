from martypy import Marty

ip="192.168.0.103"
my_marty = Marty("wifi",ip)

while(1):
    print(my_marty.foot_obstacle_sensed('left'))
    if  my_marty.foot_obstacle_sensed('left'):
        my_marty.dance()
        
    if  my_marty.foot_obstacle_sensed('right'):
        my_marty.walk(3,'auto',0,10,1500)