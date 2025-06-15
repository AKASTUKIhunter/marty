import XboxController
from connect import MartyConnection

class ControllerControl:
    def __init__(self, martyConnector: MartyConnection):
        self.martyConnector = martyConnector
        self.controller = XboxController.XboxController()

    def act(self, controls: dict):
        if controls["ljy"] > 0.5:
            self.martyConnector.WalkCase(1)
        elif controls["ljy"] < -0.5:
            self.martyConnector.MoonwalkCase(1)

        if controls["ljx"] > 0.5:
            self.martyConnector.turn("right")
        elif controls["ljx"] < -0.5:
            self.martyConnector.turn("left")

        if controls["a"]:
            self.martyConnector.moveEyes("excited")
        if controls["b"]:
            self.martyConnector.waveRightHand(100, -100)
        if controls["start"]:
            # Stop listener
            self.martyConnector.disconnect()
            return False
        else:
            # If no "start" button is not pressed, return True to keep the loop running
            return True

    def start(self):
        keep_loop = True
        while keep_loop:
            controls = self.controller.read()
            keep_loop = self.act(controls)
