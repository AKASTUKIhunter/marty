from martypy import Marty
from pynput.keyboard import Key, Listener

class KeyboardControl:
    def __init__(self, marty: Marty):
        self.marty = marty

    def on_press(self, key):
        self.key = key
        print('{0} pressed'.format(
            key))

    def on_release(self, key):
        print('{0} release'.format(
            key))
        if key == Key.up:
            self.marty.walk()
        if key == Key.down:
            pass # self.marty.
        if key == Key.left:
            self.marty.sidestep("left")
        if key == Key.right:
            self.marty.sidestep("right")
        if key == Key.space:
            self.marty.set_volume(50)
            print(self.marty.play_mp3("Everything In Its Right Place.mp3"))
        if key == Key.esc:
            # Stop listener
            self.marty.close()
            return False

    def start(self):
        print("Listener started")
        # Collect events until released
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener: # type: ignore
            listener.join()