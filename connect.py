from martypy import Marty
from martypy import MartyConnectException

def connect(ip: str):
    try:
        marty = Marty("wifi", ip)
        marty.get_ready()
        return marty
    
    except MartyConnectException as e:
        print(f"Error while connecting to Marty at {ip}: {e}")
        raise e
    except Exception as e:
        print(f"Unexpected error while connecting to Marty at {ip}: {e}")
        raise e