from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtGui, QtCore

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 350)
        self.setWindowTitle("Mr Marty")

        #Les boutons de marche
        button_avancer = QPushButton("Avancer", self)
        button_avancer.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        #button_avancer.setIcon(QtGui.QIcon('image.png'))
        #button_avancer.setIconSize(QtCore.QSize(600,60))
        button_avancer.setGeometry(900, 400, 100, 50)
        button_avancer.move(110, 100)

        button_v_droite = QPushButton("V-droite", self)
        button_v_droite.setGeometry(900, 400, 100, 50)
        button_v_droite.setStyleSheet('QPushButton {background-color: #B1E8EF; color: black;}')
        button_v_droite.move(210, 100)

        button_v_gauche = QPushButton("V-Gauche", self)
        button_v_gauche.setGeometry(900, 400, 100, 50)
        button_v_gauche.setStyleSheet('QPushButton {background-color: #B1E8EF; color: black;}')
        button_v_gauche.move(10, 100)
        

        button_droite = QPushButton("Droite", self)
        button_droite.setGeometry(900, 400, 100, 50)
        button_droite.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_droite.move(210, 150)

        button_reculer = QPushButton("Reculer", self)
        button_reculer.setGeometry(900, 400, 100, 50)
        button_reculer.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_reculer.move(110, 200)

        button_gauche = QPushButton("Gauche", self)
        button_gauche.setGeometry(900, 400, 100, 50)
        button_gauche.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_gauche.move(10, 150)

        #Slider de Vitesse
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        slider.setGeometry(900, 400, 400, 30)
        current_value = slider.value()

        slider.move(340,60)

        #Mouvement
        button_avancer = QPushButton("Avancer", self)
        button_avancer.setGeometry(900, 400, 100, 50)
        button_avancer.move(380, 120)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()