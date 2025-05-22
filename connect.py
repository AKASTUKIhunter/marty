from martypy import Marty
from martypy import MartyConnectException
from useController import ControllerControl
from useKeyboard import KeyboardControl

class MartyConnection:
    def __init__(self):
        self.ip : str
        self.marty: Marty
        self.controller: ControllerControl
        self.keyboard: KeyboardControl

    def connect(self, ip: str):
        try:
            self.marty = Marty("wifi", ip)
            self.ip = ip
            print(f"Connected to Marty at {ip}")
            self.marty.get_ready()
            self.controller = ControllerControl(self.marty)
            self.keyboard = KeyboardControl(self.marty)
            return self.marty

        except MartyConnectException as e:
            print(f"Error while connecting to Marty at {ip}: {e}")
        except Exception as e:
            print(f"Unexpected error while connecting to Marty at {ip}: {e}")