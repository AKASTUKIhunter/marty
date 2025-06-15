import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QComboBox, QLabel, QPushButton, QLineEdit
)
import os

# Fonctions pour la gestion du fichier .feels
def new_script(filename):
    with open(filename, 'wt') as script:
        pass
    return filename

def add_line(filename, cellcolor, mood, color_eyes):
    with open(filename, 'a') as script:
        line = f"{cellcolor};{mood};{color_eyes}"
        script.write(line + "\n")

# Fenêtre secondaire : éditeur .feels
class Fenetre(QWidget):
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
        self.couleur.addItems(["green","pink","cyan","red", "blue","yellow","black","ground"])

        self.feel = QComboBox()
        self.feel.addItems(["angry", "wide", "normal", "wiggle", "excited"])

        self.eyes = QComboBox()
        self.eyes.addItems([
            "#FFFFFF",  # white
            "#FF0000",  # red
            "#0000FF",  # blue
            "#FFFF00",  # yellow
            "#00FF00",  # green
            "#008080",  # teal
            "#FFC0CB",  # pink
            "#800080",  # purple
            "#FFA500"   # orange
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

# Fenêtre principale avec bouton pour ouvrir la fenêtre secondaire
class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenêtre principale")
        self.resize(400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        bouton_ouvrir = QPushButton("Ouvrir l'éditeur .feels")
        bouton_ouvrir.clicked.connect(self.ouvrir_fenetre_feels)

        layout.addWidget(QLabel("Bienvenue dans l'application principale"))
        layout.addWidget(bouton_ouvrir)

        self.fenetre_feels = None

    def ouvrir_fenetre_feels(self):
        if self.fenetre_feels is None or not self.fenetre_feels.isVisible():
            self.fenetre_feels = Fenetre()
            self.fenetre_feels.show()
        else:
            self.fenetre_feels.raise_()
            self.fenetre_feels.activateWindow()

# Lancer l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = FenetrePrincipale()
    fenetre.show()
    sys.exit(app.exec())
