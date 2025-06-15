
from pynput.keyboard import Key, Listener

class KeyboardControl:
    def __init__(self, martyConnector):
        self.martyConnector = martyConnector

    def on_press(self, key):
        self.key = key
        print('{0} pressed'.format(
            key))

    def on_release(self, key):
        print('{0} release'.format(
            key))
        if key == Key.up:
            self.martyConnector.WalkCase(1)
        elif key == Key.down:
            self.martyConnector.MoonwalkCase(1)
        elif key == Key.left:
            self.martyConnector.SideStepCaseG(1)
        elif key == Key.right:
            self.martyConnector.SideStepCaseD(1)
        elif key == Key.space:
            self.martyConnector.dance()
        elif key == Key.enter:
            self.martyConnector.get_ready()
        elif key == Key.esc:
            # Stop listener
            self.martyConnector.disconnect()
            return False

    def start(self):
        print("Listener started")
        # Collect events until released
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener: # type: ignore
            listener.join()