from martypy import Marty
from martypy import MartyConnectException

def connect(marty: Marty, ip: str):
    try:
        my_marty = Marty("wifi", ip)
        my_marty.get_ready()
    
    except MartyConnectException:
        print("Error while connecting to Marty. Couldn't connect.")