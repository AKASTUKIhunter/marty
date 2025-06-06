from gc import enable
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QSlider, QLabel, QRadioButton,QTextEdit, QSizePolicy
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QColor, QPalette
import movement


from connect import MartyConnection
import eyes
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(950, 500)
        self.setWindowTitle("Mr Marty")

        self.martyConnector = MartyConnection()

        def test():
            commands_list=text_field.toPlainText().split("\n")
            for command_elem in commands_list:
                if command_elem =="wiggle eyes":
                    eyes.moveEyes('wiggle',self.martyConnector.marty)
                elif command_elem =="forward":
                    movement.walk(1, self.martyConnector.marty)
                elif command_elem =="backward":
                    movement.walk_backwards(1, self.martyConnector.marty)
                elif command_elem =="right":
                    movement.turn("right", self.martyConnector.marty)
                elif command_elem =="left":
                    movement.turn("left", self.martyConnector.marty)
                elif command_elem =="dance":
                    self.martyConnector.marty.dance()
                elif command_elem =="celebrate":
                    self.martyConnector.marty.celebrate()
                elif command_elem =="get ready":
                    self.martyConnector.marty.get_ready()
                elif command_elem =="wave right":
                    movement.waveRightHand(0,250,self.martyConnector.marty)
                elif command_elem =="wave left":
                    movement.waveLeftHand(250,0,self.martyConnector.marty)
                else:
                    eyes.moveEyes('angry',self.martyConnector.marty)



                    
        
        


        
            
        #Commands text field
        text_field = QTextEdit(self)
        text_field.setPlaceholderText("Enter your commands")
        text_field.setSizePolicy(QSizePolicy.Policy.Fixed, 
                                 QSizePolicy.Policy.Expanding)
        palette = text_field.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor("#48DF0C")) 
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#48DF0C"))  
        text_field.setPalette(palette)
        text_field.setGeometry(350,300,550,120)
        text_field.setTextColor(QColor("#48DF0C"))
        text_field.setStyleSheet("background-color: rgb(54, 54, 54);")
        

        # Execute button
        button_execute = QPushButton("Execute  >", self)
        button_execute.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;  font-size: 13px;}')
        button_execute.setGeometry(350, 430, 135, 30)
        button_execute.clicked.connect(lambda: test())

        #IP Input
        input_field = QLineEdit(self)
        input_field.setPlaceholderText("IP address")
        input_field.setGeometry(20,300,290,30)

        # Connecting button
        button_connect = QPushButton("Connect", self)
        button_connect.setStyleSheet('QPushButton {background-color: #63FFAF; color: black;  font-size: 13px;}')
        button_connect.setGeometry(20, 350, 135, 30)

        button_connect.clicked.connect(lambda: self.martyConnector.connect(input_field.text()))

        # Disconnection button
        button_disconnect = QPushButton("Disconnect", self)
        button_disconnect.setStyleSheet('QPushButton {background-color: red; color: black;  font-size: 13px;}')
        button_disconnect.setGeometry(170, 350, 135, 30)

        button_disconnect.clicked.connect(lambda: self.martyConnector.marty.close())

        # Les boutons de marche
        button_avancer = QPushButton("", self)
        button_avancer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_avancer.setIcon(QIcon('./image/arrow-up.png')) 
        button_avancer.setIconSize(QSize(40, 40))
        button_avancer.setGeometry(110, 100, 100, 50)

        button_avancer.clicked.connect(lambda: movement.walk(1, self.martyConnector.marty))

        button_v_droite = QPushButton("", self)
        button_v_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_droite.setIcon(QIcon('./image/v-right.png'))  
        button_v_droite.setIconSize(QSize(40, 40))
        button_v_droite.setGeometry(210, 100, 100, 50)

        button_v_droite.clicked.connect(lambda: movement.turn("right", self.martyConnector.marty))

        button_v_gauche = QPushButton("", self)
        button_v_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_gauche.setIcon(QIcon('./image/v-left.png'))  
        button_v_gauche.setIconSize(QSize(40, 40))
        button_v_gauche.setGeometry(10, 100, 100, 50)

        button_v_droite.clicked.connect(lambda: movement.turn("left", self.martyConnector.marty))
        
        button_droite = QPushButton("", self)
        button_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_droite.setIcon(QIcon('./image/arrow-right.png'))  
        button_droite.setIconSize(QSize(40, 40))
        button_droite.setGeometry(210, 150, 100, 50)

        button_droite.clicked.connect(lambda: self.martyConnector.marty.sidestep("right"))

        button_reculer = QPushButton("", self)
        button_reculer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_reculer.setIcon(QIcon('./image/arrow-down.png')) 
        button_reculer.setIconSize(QSize(40, 40))
        button_reculer.setGeometry(110, 200, 100, 50)

        button_reculer.clicked.connect(lambda: movement.walk_backwards(1, self.martyConnector.marty))

        button_gauche = QPushButton("", self)
        button_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_gauche.setIcon(QIcon('./image/arrow-left.png')) 
        button_gauche.setIconSize(QSize(40, 40))
        button_gauche.setGeometry(10, 150, 100, 50)

        button_gauche.clicked.connect(lambda: self.martyConnector.marty.sidestep("left"))

        self.group = QButtonGroup()
        self.group.setExclusive(False)

        GUI_controller = QRadioButton('GUI', self)
        GUI_controller.setGeometry(55,45,50,50)
        GUI_controller.setAutoExclusive(False)
        self.group.addButton(GUI_controller)

        GUI_controller.toggled.connect(lambda: self.enable_buttons())

        self.XBOX_controller = QRadioButton('Controller', self)
        self.XBOX_controller.setGeometry(120,45,100,50)
        self.XBOX_controller.setAutoExclusive(False)
        self.group.addButton(self.XBOX_controller)
        
        self.XBOX_controller.toggled.connect(lambda: self.useController())

        self.KEYBOARD_controller = QRadioButton('Keyboard', self)
        self.KEYBOARD_controller.setGeometry(205,45,100,50)
        self.KEYBOARD_controller.setAutoExclusive(False)
        self.group.addButton(self.KEYBOARD_controller)

        self.KEYBOARD_controller.toggled.connect(lambda: self.useKeyboard())
        
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
        button_get_ready.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_get_ready.setIcon(QIcon('images/get_ready.png'))  
        button_get_ready.setIconSize(QSize(40, 40))
        button_get_ready.setGeometry(350, 120, 130, 70)
        button_get_ready.clicked.connect(lambda: self.martyConnector.marty.get_ready())

        button_celebrate = QPushButton("Celebrate", self)
        button_celebrate.setFont(font)
        button_celebrate.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_celebrate.setIcon(QIcon('images/celebrate.png'))  
        button_celebrate.setIconSize(QSize(40, 40))
        button_celebrate.setGeometry(490, 120, 130, 70)
        button_celebrate.clicked.connect(lambda: self.martyConnector.marty.celebrate())

        button_wave_left = QPushButton("Wave left", self)
        button_wave_left.setFont(font)
        button_wave_left.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wave_left.setIcon(QIcon('images/wave_left.png')) 
        button_wave_left.setIconSize(QSize(40, 40))
        button_wave_left.setGeometry(630, 120, 130, 70)
        button_wave_left.clicked.connect(lambda: movement.waveLeftHand(70,0,self.martyConnector.marty))

        button_wave_right = QPushButton("Wave right", self)
        button_wave_right.setFont(font)
        button_wave_right.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wave_right.setIcon(QIcon('images/wave_right.png'))  
        button_wave_right.setIconSize(QSize(40, 40))
        button_wave_right.setGeometry(770, 120, 130, 70)
        button_wave_right.clicked.connect(lambda: movement.waveRightHand(0,70,self.martyConnector.marty))


        # Mouvement - Ligne 2
        button_dance = QPushButton("Dance", self)
        button_dance.setFont(font)
        button_dance.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_dance.setIcon(QIcon('images/dance.png'))  
        button_dance.setIconSize(QSize(40, 40))
        button_dance.setGeometry(350, 200, 130, 70)
        button_dance.clicked.connect(lambda: self.martyConnector.marty.dance())

        button_wiggle_eyes = QPushButton("Wiggle eyes", self)
        button_wiggle_eyes.setFont(font)
        button_wiggle_eyes.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wiggle_eyes.setIcon(QIcon('images/wiggle_eyes.png')) 
        button_wiggle_eyes.setIconSize(QSize(40, 40))
        button_wiggle_eyes.setGeometry(490, 200, 130, 70)
        button_wiggle_eyes.clicked.connect(lambda: eyes.moveEyes('wiggle',self.martyConnector.marty))

        button_kick_left = QPushButton("Kick left", self)
        button_kick_left.setFont(font)
        button_kick_left.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_kick_left.setIcon(QIcon('images/kick_left.png'))  
        button_kick_left.setIconSize(QSize(40, 40))
        button_kick_left.setGeometry(630, 200, 130, 70)

        button_kick_right = QPushButton("Kick right", self)
        button_kick_right.setFont(font)
        button_kick_right.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_kick_right.setIcon(QIcon('images/kick_right.png'))  
        button_kick_right.setIconSize(QSize(40, 40))
        button_kick_right.setGeometry(770, 200, 130, 70)

    def disable_buttons(self):
        # Disable all buttons except the connect and disconnect button
        for button in self.findChildren(QPushButton):
            if button.text() not in ["Connect", "Disconnect"]:
                button.setEnabled(False)
        for button in self.group.buttons():
            # if button is not radioButton:
            button.setEnabled(False)

    def enable_buttons(self):
        # Enable all buttons except the connect and disconnect button
        for button in self.findChildren(QPushButton):
            if button.text() not in ["Connect", "Disconnect"]:
                button.setEnabled(True)

    def uncheck_QRadio_buttons(self):
        # Uncheck every other button in this group
        for button in self.group.buttons():
            # if button is not radioButton:
                button.setChecked(False)

    def useKeyboard(self):
        self.uncheck_QRadio_buttons()
        self.disable_buttons()
        self.martyConnector.keyboard.start()

    def useController(self):
        self.disable_buttons()
        self.martyConnector.controller.start()
        self.uncheck_QRadio_buttons()
