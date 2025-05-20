import XboxController

from martypy import Marty

class ControllerControl:
    def __init__(self, marty: Marty):
        self.marty = marty
        self.controller = XboxController.XboxController()

    def act(self, controls: dict):
        if controls["ljy"] > 0.5:
            self.marty.walk()
        elif controls["ljy"] < -0.5:
            pass
        
        if controls["ljx"] > 0.5:
            self.marty.sidestep("right")
        elif controls["ljx"] < -0.5:
            self.marty.sidestep("left")

        if controls["a"]:
            self.marty.set_volume(100)
            print(self.marty.play_mp3("Everything In Its Right Place.mp3"))
        if controls["start"]:
            # Stop listener
            self.marty.close()
            return False
        else:
            # If no "start" button is not pressed, return True to keep the loop running
            return True

    def start(self):
        keep_loop = True
        while keep_loop:
            controls = self.controller.read()
            keep_loop = self.act(controls)
