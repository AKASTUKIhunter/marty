from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 350)
        self.setWindowTitle("Mr Marty")
 
        button_avancer = QPushButton("Avancer", self)
        button_avancer.setGeometry(900, 400, 100, 50)
        button_avancer.move(110, 100)

        button_reculer = QPushButton("V-droite", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.move(210, 100)

        button_reculer = QPushButton("V-Gauche", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.move(10, 100)
        

        button_reculer = QPushButton("Droite", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.move(210, 150)

        button_reculer = QPushButton("Reculer", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.move(110, 200)

        button_reculer = QPushButton("Gauche", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.move(10, 150)

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        slider.setGeometry(900, 400, 400, 30)

        

        current_value = slider.value()

        slider.move(340,50)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()