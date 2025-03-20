from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from assets.pokemon import *
import requests

# créer nouvelle fenêtre pour afficher les informations sur un pokémon
# afficher le nom, le type, la taille et le poids du pokémon
# afficher une image du pokémon
# afficher un bouton pour fermer la fenêtre
# afficher sa sous-évolution si elle existe 
# afficher son évolution si elle existe
# affiche sa faiblesse si elle existe


class Pokeinfo(QWidget):
    def __init__(self, pokedex_id):
        super().__init__()
        self.setWindowTitle("Pokeinfo")
        self.setGeometry(100, 100, 500, 500)
        self.pokemon = Pokemon(pokedex_id)
        self.setWindowTitle(self.pokemon.french_name())
        x = requests.get(self.pokemon.image_links()["hires"], stream=True)
        image = QImage()
        image.loadFromData(x.content)
        image.scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio)
        self.setWindowIcon(QIcon(QPixmap().fromImage(image)))
        self.closeButton = QPushButton("Close")
        self.closeButton.clicked.connect(self.close)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.closeButton)