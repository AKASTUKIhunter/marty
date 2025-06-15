from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QLabel
import sys

class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenêtre pop-up")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ceci est une fenêtre pop-up."))
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fenêtre principale")
        self.resize(300, 200)

        button = QPushButton("Ouvrir la pop-up", self)
        button.clicked.connect(self.show_popup)

    def show_popup(self):
        popup = PopupWindow()
        popup.exec()  # ouvre en mode modal (bloque la fenêtre principale)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
