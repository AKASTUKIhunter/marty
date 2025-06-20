from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLineEdit, QSlider, QLabel, QRadioButton, QButtonGroup, QTextEdit, QSizePolicy
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QFont, QColor, QPalette
import os
from connect import MartyConnection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(950, 550)
        self.setWindowTitle("Mr Marty")
        self.w = None

        self.martyConnector = MartyConnection()

        def test():
            if hasattr(self.martyConnector, 'marty') and self.martyConnector.marty is None:
                commands_list = text_field.toPlainText().split("\n")
                for command_elem in commands_list:
                    if command_elem == "wiggle eyes":
                        self.martyConnector.moveEyes('wiggle')
                    elif command_elem == "forward":
                        self.martyConnector.WalkCase(1)
                    elif command_elem == "backward":
                        self.martyConnector.MoonwalkCase(1)
                    elif command_elem == "right":
                        self.martyConnector.turn("right")
                    elif command_elem == "left":
                        self.martyConnector.turn("left")
                    elif command_elem == "dance":
                        self.martyConnector.dance()
                    elif command_elem == "celebrate":
                        self.martyConnector.celebrate()
                    elif command_elem == "get ready":
                        self.martyConnector.get_ready()
                    elif command_elem == "wave right":
                        self.martyConnector.waveRightHand(0, 250)
                    elif command_elem == "wave left":
                        self.martyConnector.waveLeftHand(250, 0)
                    elif command_elem == "kick left":
                        self.martyConnector.kickLeft()
                    elif command_elem == "kick right":
                        self.martyConnector.kickRight()
                    elif command_elem == "turn right":
                        self.martyConnector.turn("right")
                    elif command_elem == "turn left":
                        self.martyConnector.turn("left")
                    else:
                        self.martyConnector.moveEyes('angry')

        # Commands text field
        text_field = QTextEdit(self)
        text_field.setPlaceholderText("Enter your commands")
        text_field.setSizePolicy(QSizePolicy.Policy.Fixed, 
                                QSizePolicy.Policy.Expanding)
        palette = text_field.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor("#48DF0C")) 
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#48DF0C"))  
        text_field.setPalette(palette)
        text_field.setGeometry(350, 300, 550, 120)
        text_field.setTextColor(QColor("#48DF0C"))
        text_field.setStyleSheet("background-color: rgb(54, 54, 54);")

        # Execute button
        button_execute = QPushButton("Execute >", self)
        button_execute.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;  font-size: 13px;}')
        button_execute.setGeometry(348, 392, 135, 30)
        button_execute.clicked.connect(lambda: test())

        # Calibration button
        button_calibration = QPushButton("Calibration", self)
        button_calibration.setStyleSheet('QPushButton {background-color: red; color: black;  font-size: 13px;}')
        button_calibration.setGeometry(770, 450, 135, 30)
        button_calibration.clicked.connect(lambda: self.martyConnector.calibrateColors(button_calibration))

        # IP Input
        input_field = QLineEdit(self)
        input_field.setPlaceholderText("IP address")
        input_field.setGeometry(20, 300, 290, 30)

        # Connecting button
        button_connect = QPushButton("Connect", self)
        button_connect.setStyleSheet('QPushButton {background-color: #63FFAF; color: black;  font-size: 13px;}')
        button_connect.setGeometry(20, 350, 135, 30)
        button_connect.clicked.connect(lambda: self.martyConnector.connect(input_field.text()))

        # Disconnection button
        button_disconnect = QPushButton("Disconnect", self)
        button_disconnect.setStyleSheet('QPushButton {background-color: red; color: black;  font-size: 13px;}')
        button_disconnect.setGeometry(170, 350, 135, 30)
        button_disconnect.clicked.connect(lambda: self.martyConnector.disconnect())

        # File Dance Input
        input_field_dance = QLineEdit(self)
        input_field_dance.setPlaceholderText("Dance File name")
        input_field_dance.setGeometry(20, 410, 145, 30)

        # File Dance button
        button_read_dance = QPushButton("Read .dance file", self)
        button_read_dance.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;  font-size: 13px;}')
        button_read_dance.setGeometry(20, 450, 135, 30)
        button_read_dance.clicked.connect(lambda: self.martyConnector.lecture_dance(input_field_dance.text()))

        # File Feel Input
        input_field_feel = QLineEdit(self)
        input_field_feel.setPlaceholderText("Feel File name")
        input_field_feel.setGeometry(175, 410, 145, 30)

        #file Feel button
        button_read_feel = QPushButton("Read .feel file", self)
        button_read_feel.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;  font-size: 13px;}')
        button_read_feel.setGeometry(175, 450, 135, 30)

        button_read_feel.clicked.connect(lambda: self.martyConnector.feelScraper.getFeels(input_field_feel.text()))

        # Movement buttons
        button_avancer = QPushButton("", self)
        button_avancer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_avancer.setIcon(QIcon('./image/arrow-up.png')) 
        button_avancer.setIconSize(QSize(40, 40))
        button_avancer.setGeometry(110, 100, 100, 50)
        button_avancer.clicked.connect(lambda: self.handle_button_click("avancer"))

        button_v_droite = QPushButton("", self)
        button_v_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_droite.setIcon(QIcon('./image/v-right.png'))  
        button_v_droite.setIconSize(QSize(40, 40))
        button_v_droite.setGeometry(210, 100, 100, 50)
        button_v_droite.clicked.connect(lambda: self.handle_button_click("v_droite"))

        button_v_gauche = QPushButton("", self)
        button_v_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_v_gauche.setIcon(QIcon('./image/v-left.png'))  
        button_v_gauche.setIconSize(QSize(40, 40))
        button_v_gauche.setGeometry(10, 100, 100, 50)
        button_v_gauche.clicked.connect(lambda: self.handle_button_click("v_gauche"))

        button_droite = QPushButton("", self)
        button_droite.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_droite.setIcon(QIcon('./image/arrow-right.png'))  
        button_droite.setIconSize(QSize(40, 40))
        button_droite.setGeometry(210, 150, 100, 50)
        button_droite.clicked.connect(lambda: self.handle_button_click("droite"))

        button_reculer = QPushButton("", self)
        button_reculer.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_reculer.setIcon(QIcon('./image/arrow-down.png')) 
        button_reculer.setIconSize(QSize(40, 40))
        button_reculer.setGeometry(110, 200, 100, 50)
        button_reculer.clicked.connect(lambda: self.handle_button_click("reculer"))

        button_gauche = QPushButton("", self)
        button_gauche.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_gauche.setIcon(QIcon('./image/arrow-left.png')) 
        button_gauche.setIconSize(QSize(40, 40))
        button_gauche.setGeometry(10, 150, 100, 50)
        button_gauche.clicked.connect(lambda: self.handle_button_click("gauche"))


        self.writingGroup = QButtonGroup()
        self.writingGroup.setExclusive(True)

        # Radio buttons for SEQ and ABS
        self.writing_seq = QRadioButton('SEQ', self)
        self.writing_seq.setGeometry(55, 250, 100, 50)
        self.writing_seq.setAutoExclusive(False)
        self.writingGroup.addButton(self.writing_seq)

        self.writing_abs = QRadioButton('ABS', self)
        self.writing_abs.setGeometry(120, 250, 100, 50)
        self.writing_abs.setAutoExclusive(False)
        self.writingGroup.addButton(self.writing_abs)

        self.GUIgroup = QButtonGroup()
        self.GUIgroup.setExclusive(True)

        # Radio buttons for controllers
        GUI_controller = QRadioButton('GUI', self)
        GUI_controller.setGeometry(55, 45, 50, 50)
        GUI_controller.setAutoExclusive(False)
        self.GUIgroup.addButton(GUI_controller)
        GUI_controller.toggled.connect(lambda: self.enable_buttons())

        XBOX_controller = QRadioButton('Controller', self)
        XBOX_controller.setGeometry(120, 45, 100, 50)
        XBOX_controller.setAutoExclusive(False)
        self.GUIgroup.addButton(XBOX_controller)
        XBOX_controller.toggled.connect(lambda: self.useController())

        KEYBOARD_controller = QRadioButton('Keyboard', self)
        KEYBOARD_controller.setGeometry(205, 45, 100, 50)
        KEYBOARD_controller.setAutoExclusive(False)
        self.GUIgroup.addButton(KEYBOARD_controller)
        KEYBOARD_controller.toggled.connect(lambda: self.useKeyboard())

        # Title
        Title = QLabel("Choose a controller", self)
        Title.setGeometry(100, 15, 500, 50)
        font1 = QFont("Arial", 10)
        Title.setFont(font1)

        # Slider for speed
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        slider.setGeometry(350, 70, 543, 30)

        # Slider titles
        Title_slider1 = QLabel("🐌 Slow", self)
        Title_slider1.setGeometry(355, 25, 500, 50)
        font2 = QFont("Arial", 11)
        Title_slider1.setFont(font2)

        Title_slider2 = QLabel("⚡Fast", self)
        Title_slider2.setGeometry(860, 25, 500, 50)
        Title_slider2.setFont(font2)

        # Movement buttons - Row 1
        button_get_ready = QPushButton("Get ready", self)
        font = QFont("Arial", 12, QFont.Weight.Bold)
        button_get_ready.setFont(font)
        button_get_ready.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_get_ready.setIcon(QIcon('images/get_ready.png'))  
        button_get_ready.setIconSize(QSize(40, 40))
        button_get_ready.setGeometry(350, 120, 130, 70)
        button_get_ready.clicked.connect(lambda: self.handle_button_click("get_ready"))

        button_celebrate = QPushButton("Celebrate", self)
        button_celebrate.setFont(font)
        button_celebrate.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_celebrate.setIcon(QIcon('images/celebrate.png'))  
        button_celebrate.setIconSize(QSize(40, 40))
        button_celebrate.setGeometry(490, 120, 130, 70)
        button_celebrate.clicked.connect(lambda: self.handle_button_click("celebrate"))

        button_wave_left = QPushButton("Wave left", self)
        button_wave_left.setFont(font)
        button_wave_left.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wave_left.setIcon(QIcon('images/wave_left.png')) 
        button_wave_left.setIconSize(QSize(40, 40))
        button_wave_left.setGeometry(630, 120, 130, 70)
        button_wave_left.clicked.connect(lambda: self.handle_button_click("wave_left"))

        button_wave_right = QPushButton("Wave right", self)
        button_wave_right.setFont(font)
        button_wave_right.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wave_right.setIcon(QIcon('images/wave_right.png'))  
        button_wave_right.setIconSize(QSize(40, 40))
        button_wave_right.setGeometry(770, 120, 130, 70)
        button_wave_right.clicked.connect(lambda: self.handle_button_click("wave_right"))

        # Movement buttons - Row 2
        button_dance = QPushButton("Dance", self)
        button_dance.setFont(font)
        button_dance.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_dance.setIcon(QIcon('images/dance.png'))  
        button_dance.setIconSize(QSize(40, 40))
        button_dance.setGeometry(350, 200, 130, 70)
        button_dance.clicked.connect(lambda: self.handle_button_click("dance"))

        button_wiggle_eyes = QPushButton("Wiggle eyes", self)
        button_wiggle_eyes.setFont(font)
        button_wiggle_eyes.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_wiggle_eyes.setIcon(QIcon('images/wiggle_eyes.png')) 
        button_wiggle_eyes.setIconSize(QSize(40, 40))
        button_wiggle_eyes.setGeometry(490, 200, 130, 70)
        button_wiggle_eyes.clicked.connect(lambda: self.handle_button_click("wiggle_eyes"))

        button_kick_left = QPushButton("Kick left", self)
        button_kick_left.setFont(font)
        button_kick_left.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_kick_left.setIcon(QIcon('images/kick_left.png'))  
        button_kick_left.setIconSize(QSize(40, 40))
        button_kick_left.setGeometry(630, 200, 130, 70)
        button_kick_left.clicked.connect(lambda: self.handle_button_click("kick_left"))

        button_kick_right = QPushButton("Kick right", self)
        button_kick_right.setFont(font)
        button_kick_right.setStyleSheet('QPushButton {background-color: #03b8ff; color: black;}')
        button_kick_right.setIcon(QIcon('images/kick_right.png'))  
        button_kick_right.setIconSize(QSize(40, 40))
        button_kick_right.setGeometry(770, 200, 130, 70)
        button_kick_right.clicked.connect(lambda: self.handle_button_click("kick_right"))

        button_create_feel = QPushButton("Create .feel", self)
        button_create_feel.setStyleSheet('QPushButton {background-color: #03b8ff; color: black; font-size: 13px;}')
        button_create_feel.setGeometry(175, 500, 135, 30)
        button_create_feel.clicked.connect(lambda: self.showNewWindow())

        GUI_controller.setChecked(True)  # Set GUI as default controller

    def handle_button_click(self, action):
        if hasattr(self.martyConnector, 'marty') and self.martyConnector.marty is not None:
            if self.writing_seq.isChecked():
                if action == "avancer":
                    self.martyConnector.Addline("1U","new_dance_seq.dance")
                elif action == "reculer":
                    self.martyConnector.Addline("1B","new_dance_seq.dance")
                elif action == "v_droite":
                    self.martyConnector.Addline("1R","new_dance_seq.dance")
                elif action == "v_gauche":
                    self.martyConnector.Addline("1L","new_dance_seq.dance")
                elif action == "droite":
                    self.martyConnector.Addline("1R","new_dance_seq.dance")
                elif action == "gauche":
                    self.martyConnector.Addline("1L","new_dance_seq.dance")
            elif self.writing_abs.isChecked():
                if action == "avancer":
                    self.martyConnector.writing_file_abs("avancer","new_dance_seq.dance")
                elif action == "reculer":
                    self.martyConnector.writing_file_abs("reculer","new_dance_seq.dance")
                elif action == "v_droite":
                    self.martyConnector.writing_file_abs("droite","new_dance_seq.dance")
                elif action == "v_gauche":
                    self.martyConnector.writing_file_abs("gauche","new_dance_seq.dance")
                elif action == "droite":
                    self.martyConnector.writing_file_abs("droite","new_dance_seq.dance")
                elif action == "gauche":
                    self.martyConnector.writing_file_abs("gauche","new_dance_seq.dance")
            else:
                if action == "avancer":
                    self.martyConnector.WalkCase(1)
                elif action == "reculer":
                    self.martyConnector.MoonwalkCase(1)
                elif action == "v_droite":
                    self.martyConnector.turn("right")
                elif action == "v_gauche":
                    self.martyConnector.turn("left")
                elif action == "droite":
                    self.martyConnector.SideStepCaseD(1)
                elif action == "gauche":
                    self.martyConnector.SideStepCaseG(1)
                elif action == "get_ready":
                    self.martyConnector.get_ready()
                elif action == "celebrate":
                    self.martyConnector.celebrate()
                elif action == "wave_left":
                    self.martyConnector.waveLeftHand(70, 0)
                elif action == "wave_right":
                    self.martyConnector.waveRightHand(0, 70)
                elif action == "dance":
                    self.martyConnector.dance()
                elif action == "wiggle_eyes":
                    self.martyConnector.moveEyes('wiggle')
                elif action == "kick_left":
                    self.martyConnector.kickLeft()
                elif action == "kick_right":
                    self.martyConnector.kickRight()

    def disable_buttons(self):
        # Disable all buttons except the connect and disconnect button
        for button in self.findChildren(QPushButton):
            if button.text() not in ["Connect", "Disconnect"]:
                button.setEnabled(False)
        for button in self.GUIgroup.buttons():
            button.setEnabled(False)

    def enable_buttons(self):
        # Enable all buttons except the connect and disconnect button
        for button in self.findChildren(QPushButton):
            if button.text() not in ["Connect", "Disconnect"]:
                button.setEnabled(True)

    def uncheck_QRadio_buttons(self):
        # Uncheck every other button in this group
        for button in self.GUIgroup.buttons():
            button.setChecked(False)

    def useKeyboard(self):
        if hasattr(self.martyConnector, 'keyboard') and self.martyConnector.keyboard is not None:
            self.uncheck_QRadio_buttons()
            self.disable_buttons()
            self.martyConnector.keyboard.start()
        else:
            print("Marty connection not established yet.")
            self.uncheck_QRadio_buttons()

    def useController(self):
        if hasattr(self.martyConnector, 'controller') and self.martyConnector.controller is not None:
            self.disable_buttons()
            self.martyConnector.controller.start()
            self.uncheck_QRadio_buttons()
        else:
            print("Marty connection not established yet.")
            self.uncheck_QRadio_buttons()

    def showNewWindow(self):
        if self.w is None:
            self.w = FeelsCreatorWindow()
            self.w.show()

class FeelsCreatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Écriture .feels")
        self.resize(950, 200)

        self.script_name = None  

        # Layout principal
        main_layout = QVBoxLayout()

        # Champ pour entrer le nom du fichier
        file_layout = QHBoxLayout()
        file_layout.addWidget(QLabel("Nom du fichier (.feels):"))
        self.filename_input = QLineEdit()
        file_layout.addWidget(self.filename_input)
        main_layout.addLayout(file_layout)

        # Layout horizontal pour les combos
        combo_layout = QHBoxLayout()

        self.couleur = QComboBox()
        self.couleur.addItems(["red", "green", "blue", "yellow", "purple", "pink", "black"])

        self.feel = QComboBox()
        self.feel.addItems(["angry", "wide", "normal", "wiggle", "excited"])

        self.eyes = QComboBox()
        self.eyes.addItems([
            "#FF0000",  # red
            "#00FF00",  # green
            "#0000FF",  # blue
            "#FFFF00",  # yellow
            "#FFC0CB",  # pink
            "#800080",  # purple
            "#000000",  # black
        ])

        combo_layout.addWidget(QLabel("Cell Color:"))
        combo_layout.addWidget(self.couleur)
        combo_layout.addWidget(QLabel("Mood:"))
        combo_layout.addWidget(self.feel)
        combo_layout.addWidget(QLabel("Eye Color:"))
        combo_layout.addWidget(self.eyes)

        main_layout.addLayout(combo_layout)

        self.bouton = QPushButton("Ajouter à .feels")
        self.bouton.clicked.connect(self.sauvegarder_choix)

        self.retour = QLabel("")

        main_layout.addWidget(self.bouton)
        main_layout.addWidget(self.retour)

        self.setLayout(main_layout)

    def sauvegarder_choix(self):
        filename = self.filename_input.text().strip()

        if not filename:
            self.retour.setText("Entrez un nom de fichier valide.")
            return

        if not filename.endswith(".feels"):
            filename += ".feels"

        self.script_name = filename

        if not os.path.exists(self.script_name):
            new_script(self.script_name)

        couleur = self.couleur.currentText()
        humeur = self.feel.currentText()
        yeux = self.eyes.currentText()

        add_line(self.script_name, couleur, humeur, yeux)
        self.retour.setText(f" Ligne ajoutée à {self.script_name} : {couleur};{humeur};{yeux}")


def new_script(filename):
    with open(filename, 'wt') as script:
        pass
    return filename

def add_line(filename, cellcolor, mood, color_eyes):
    with open(filename, 'a') as script:
        line = f"{cellcolor};{mood};{color_eyes}"
        script.write(line + "\n")