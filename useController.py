import XboxController
from movement import *

from martypy import Marty

import movement

class ControllerControl:
    def __init__(self, marty: Marty):
        self.marty = marty
        self.controller = XboxController.XboxController()

    def act(self, controls: dict):
        if controls["ljy"] > 0.5:
            self.marty.walk()
        elif controls["ljy"] < -0.5:
            movement.walk_backwards(5, self.marty)
        
        if controls["ljx"] > 0.5:
            movement.turn("right", self.marty)
        elif controls["ljx"] < -0.5:
            movement.turn("left", self.marty)

        if controls["a"]:
            self.marty.set_volume(100)
            movement.moveEyes("excited", self.marty)
        if controls["b"]:
            movement.moveArms(100, -100, self.marty)
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
