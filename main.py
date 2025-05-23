import connect
import useController
import useKeyboard
import interface
import sys
from PyQt6.QtWidgets import QApplication

try:
    app = QApplication(sys.argv)
    window = interface.MainWindow()
    window.show()
    app.exec()
except Exception as e:
    print(f"Error: {e}")
