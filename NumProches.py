import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QMenuBar, QMenu, QAction, QStatusBar, QHBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

def find_closest_factors_with_min_gap(x):
    """
    Trouve deux entiers a et b proches de x (avec un écart minimal entre eux)
    tels que a * b = x.

    :param x: Un entier positif.
    :return: Un tuple (a, b) avec un écart minimal entre a et b.
    """
    if x <= 0:
        raise ValueError("L'entier x doit être strictement positif.")

    root = int(math.sqrt(x))
    for i in range(root, 0, -1):
        if x % i == 0:
            a, b = i, x // i
            return a, b
    return None

class FactorFinderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("NumProches")
        self.setGeometry(100, 100, 500, 400)

        # Personnalisation des couleurs
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 248, 255))
        self.setPalette(palette)

        # Créer une barre d'état
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet("background-color: #f0f0f0;")
        self.setStatusBar(self.statusBar)

        # Ajouter une barre de menu
        menuBar = self.menuBar()

        # Onglet "Fichier"
        fileMenu = menuBar.addMenu("Fichier")
        quitAction = QAction("Quitter", self)
        quitAction.triggered.connect(self.close)
        fileMenu.addAction(quitAction)

        # Onglet "Aide"
        helpMenu = menuBar.addMenu("Aide")
        aboutAction = QAction("À propos", self)
        aboutAction.triggered.connect(self.showAboutDialog)
        helpMenu.addAction(aboutAction)

        # Créer le widget central
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # Ajouter un titre stylisé
        title = QLabel("NumProches")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.label = QLabel("Entrez un entier positif :")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)

        # Zone de saisie avec style
        self.inputField = QLineEdit(self)
        self.inputField.setFont(QFont("Arial", 12))
        self.inputField.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")
        self.inputField.returnPressed.connect(self.onFindFactors)  # Liaison de la touche Entrée
        layout.addWidget(self.inputField)

        # Bouton stylisé
        self.findButton = QPushButton("Trouver les facteurs", self)
        self.findButton.setFont(QFont("Arial", 12))
        self.findButton.setStyleSheet("padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        self.findButton.clicked.connect(self.onFindFactors)
        layout.addWidget(self.findButton)

        self.resultLabel = QLabel("")
        self.resultLabel.setFont(QFont("Arial", 12))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setStyleSheet("margin-top: 15px;")
        layout.addWidget(self.resultLabel)

        # Ajouter un pied de page stylisé
        footer = QLabel("Créé par Ralph Masson - 2024")
        footer.setFont(QFont("Arial", 10, QFont.StyleItalic))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: gray; margin-top: 20px;")
        layout.addWidget(footer)

        centralWidget.setLayout(layout)

    def onFindFactors(self):
        try:
            x = int(self.inputField.text())
            if x <= 0:
                raise ValueError

            factors = find_closest_factors_with_min_gap(x)
            if factors:
                self.resultLabel.setText(f"Les facteurs proches de {x} sont {factors[0]} et {factors[1]}.")
                self.statusBar.showMessage("Facteurs trouvés avec succès.")
            else:
                self.resultLabel.setText("Aucun facteur trouvé.")
                self.statusBar.showMessage("Aucun facteur trouvé.")

        except ValueError:
            self.resultLabel.setText("Veuillez entrer un entier positif valide.")
            self.statusBar.showMessage("Entrée invalide.")

    def showAboutDialog(self):
        self.resultLabel.setText("Application pour trouver les facteurs proches d'un entier.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FactorFinderApp()
    window.show()
    sys.exit(app.exec_())
