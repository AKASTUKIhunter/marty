from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon, QFont
import sys



import connect
import eyes

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(950, 350)
        self.setWindowTitle("Mr Marty")

        #IP Input
        input_field = QLineEdit(self)
        input_field.setPlaceholderText("IP address")
        input_field.setGeometry(20,300,200,30)

        # Bouton Se connecter
        button_connect = QPushButton("Connect", self)
        button_connect.setStyleSheet('QPushButton {background-color: #63FFAF; color: black;  font-size: 13px;}')
        button_connect.setGeometry(230, 300, 150, 30)
        
        

        button_disconnect = QPushButton("Disconnect", self)
        button_disconnect.setStyleSheet('QPushButton {background-color: red; color: black;  font-size: 13px;}')
        button_disconnect.setGeometry(400, 300, 150, 30)

        
        #boutton de connection 
        button_connect.clicked.connect(lambda: connect.connect(input_field.text()))

        
        

        # Les boutons de marche
        button_avancer = QPushButton("", self)
        button_avancer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_avancer.setIcon(QIcon('./image/arrow-up.png')) 
        button_avancer.setIconSize(QSize(40, 40))
        button_avancer.setGeometry(110, 100, 100, 50)

        button_v_droite = QPushButton("", self)
        button_v_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_droite.setIcon(QIcon('./image/v-right.png'))  
        button_v_droite.setIconSize(QSize(40, 40))
        button_v_droite.setGeometry(210, 100, 100, 50)

        button_v_gauche = QPushButton("", self)
        button_v_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_gauche.setIcon(QIcon('./image/v-left.png'))  
        button_v_gauche.setIconSize(QSize(40, 40))
        button_v_gauche.setGeometry(10, 100, 100, 50)

        button_droite = QPushButton("", self)
        button_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_droite.setIcon(QIcon('./image/arrow-right.png'))  
        button_droite.setIconSize(QSize(40, 40))
        button_droite.setGeometry(210, 150, 100, 50)

        button_reculer = QPushButton("", self)
        button_reculer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_reculer.setIcon(QIcon('./image/arrow-down.png')) 
        button_reculer.setIconSize(QSize(40, 40))
        button_reculer.setGeometry(110, 200, 100, 50)

        button_gauche = QPushButton("", self)
        button_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_gauche.setIcon(QIcon('./image/arrow-left.png')) 
        button_gauche.setIconSize(QSize(40, 40))
        button_gauche.setGeometry(10, 150, 100, 50)

        GUI_controller = QRadioButton('GUI', self)
        GUI_controller.setGeometry(55,45,50,50)

        GUI_controller = QRadioButton('Controller', self)
        GUI_controller.setGeometry(120,45,100,50)

        GUI_controller = QRadioButton('Keyboard', self)
        GUI_controller.setGeometry(205,45,100,50)

        Title = QLabel("Choose a controller", self)
        Title.setGeometry(100,15,500,50)
        font1 = QFont("Arial", 10)
        Title.setFont(font1)

        # Slider de Vitesse
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        slider.setGeometry(350, 70, 543, 30)

        #Titles of the Slider(Slow)
        Title_slider1 = QLabel("🐌 Slow", self)
        Title_slider1.setGeometry(355,25,500,50)
        font2 = QFont("Arial", 11)
        Title_slider1.setFont(font2)

        #Titles of the Slider (Fast)
        Title_slider2 = QLabel("⚡Fast", self)
        Title_slider2.setGeometry(860,25,500,50)
        Title_slider2.setFont(font2)

        # Mouvement - Ligne 1
        button_get_ready = QPushButton("Get ready", self)
        font = QFont("Arial", 12, QFont.Weight.Bold)
        button_get_ready.setFont(font)
        button_get_ready.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_get_ready.setIcon(QIcon('images/get_ready.png'))  
        button_get_ready.setIconSize(QSize(40, 40))
        button_get_ready.setGeometry(350, 120, 130, 70)

        button_celebrate = QPushButton("Celebrate", self)
        button_celebrate.setFont(font)
        button_celebrate.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_celebrate.setIcon(QIcon('images/celebrate.png'))  
        button_celebrate.setIconSize(QSize(40, 40))
        button_celebrate.setGeometry(490, 120, 130, 70)

        button_wave_left = QPushButton("Wave left", self)
        button_wave_left.setFont(font)
        button_wave_left.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_wave_left.setIcon(QIcon('images/wave_left.png')) 
        button_wave_left.setIconSize(QSize(40, 40))
        button_wave_left.setGeometry(630, 120, 130, 70)

        button_wave_right = QPushButton("Wave right", self)
        button_wave_right.setFont(font)
        button_wave_right.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_wave_right.setIcon(QIcon('images/wave_right.png'))  
        button_wave_right.setIconSize(QSize(40, 40))
        button_wave_right.setGeometry(770, 120, 130, 70)

        # Mouvement - Ligne 2
        button_dance = QPushButton("Dance", self)
        button_dance.setFont(font)
        button_dance.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_dance.setIcon(QIcon('images/dance.png'))  
        button_dance.setIconSize(QSize(40, 40))
        button_dance.setGeometry(350, 200, 130, 70)

        button_wiggle_eyes = QPushButton("Wiggle eyes", self)
        button_wiggle_eyes.setFont(font)
        button_wiggle_eyes.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_wiggle_eyes.setIcon(QIcon('images/wiggle_eyes.png')) 
        button_wiggle_eyes.setIconSize(QSize(40, 40))
        button_wiggle_eyes.setGeometry(490, 200, 130, 70)
        button_wiggle_eyes.clicked.connect(lambda: eyes.moveEyes('wiggle'))

        button_kick_left = QPushButton("Kick left", self)
        button_kick_left.setFont(font)
        button_kick_left.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_kick_left.setIcon(QIcon('images/kick_left.png'))  
        button_kick_left.setIconSize(QSize(40, 40))
        button_kick_left.setGeometry(630, 200, 130, 70)

        button_kick_right = QPushButton("Kick right", self)
        button_kick_right.setFont(font)
        button_kick_right.setStyleSheet('QPushButton {background-color: #2AD0E2; color: black;}')
        button_kick_right.setIcon(QIcon('images/kick_right.png'))  
        button_kick_right.setIconSize(QSize(40, 40))
        button_kick_right.setGeometry(770, 200, 130, 70)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()