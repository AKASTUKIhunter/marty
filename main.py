import connect
import useController
import useKeyboard
import interface
import sys
from PyQt6.QtWidgets import QApplication

# marty = connect.connect("192.168.0.103")

# method = input("Enter 'c' for controller or 'k' for keyboard: ")
# if method == 'c':
#     c = useController.ControllerControl(marty)
#     c.start()

# elif method == 'k':
#     k = useKeyboard.KeyboardControl(marty)
#     k.start()

try:
    app = QApplication(sys.argv)
    window = interface.MainWindow()
    window.show()
    app.exec()
except Exception as e:
    print(f"Error: {e}")
