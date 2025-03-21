from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from assets.pokemon import *
from assets.constante import BDD
import json
import requests


with open(BDD, encoding="utf8") as f:
    data = json.load(f)

class Pokeinfo(QWidget):
    """Va afficher les informations d'un pokemon
    """
    def __init__(self, pokedex_id):
        super().__init__()
        self.setGeometry(100, 100, 350, 500)
        self.update_data()
        if pokedex_id in data["users"][data["lastConnected"]]["pokedex"]:
            self.pokemon = Pokemon(pokedex_id)
            self.setWindowTitle(self.pokemon.french_name())
            x = requests.get(self.pokemon.image_links()["thumbnail"], stream=True)
            image = QImage()
            image.loadFromData(x.content)
            image.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio)
            self.setWindowIcon(QIcon(QPixmap().fromImage(image)))
            self.closeButton = QPushButton("Close")
            self.closeButton.clicked.connect(self.close)
            self.final_layout = QGridLayout()
            self.info_layout = QVBoxLayout()
            self.info_layout.addWidget(QLabel(f"Nom : {self.pokemon.french_name()} ({self.pokemon.pokedex_id})"))
            self.info_layout.addWidget(QLabel(f"Type : {self.pokemon.his_type()}"))
            self.info_layout.addWidget(QLabel(f"Taille : {self.pokemon.height()}"))
            self.info_layout.addWidget(QLabel(f"Poids : {self.pokemon.weight()}"))
            self.info_layout.addWidget(QLabel(f"HP : {self.pokemon.hp()}"))
            self.info_layout.addWidget(QLabel(f"Génération : {self.pokemon.generation()}"))
            if self.pokemon.evolution() != None:
                self.info_layout.addWidget(QLabel(f"Evolution : {Pokemon(self.pokemon.evolution()).french_name()}"))
            if self.pokemon.pre_evolution() != None:
                if self.pokemon.pre_pre_evo() != None:
                    self.info_layout.addWidget(QLabel(f"Sous-évolutions : {Pokemon(self.pokemon.pre_pre_evo()).french_name()} et {Pokemon(self.pokemon.pre_evolution()).french_name()} "))
                else: 
                    self.info_layout.addWidget(QLabel(f"Sous-évolution : {Pokemon(self.pokemon.pre_evolution()).french_name()}"))
            self.info_layout.addWidget(QLabel(f"Faiblesse : {ENGLISH_TYPE_TO_FRENCH_DICT[self.pokemon.weakness()]}"))
            self.info_layout.addWidget(self.closeButton, alignment=Qt.AlignBottom)
            self.image = QLabel()
            self.image.setPixmap(QPixmap.fromImage(image))
            self.final_layout.addLayout(self.info_layout, 0, 0)
            self.final_layout.addWidget(self.image, 0, 1)
            self.setLayout(self.final_layout)
        else:
            self.pokemon = Pokemon(pokedex_id)
            self.setWindowTitle("???")
            x = requests.get(self.pokemon.image_links()["thumbnail"], stream=True)
            image = QImage()
            image.loadFromData(x.content)
            image.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio)
            img = image.convertToFormat(QImage.Format_Alpha8)
            self.setWindowIcon(QIcon(QPixmap().fromImage(img)))
            self.closeButton = QPushButton("Close")
            self.closeButton.clicked.connect(self.close)
            self.final_layout = QGridLayout()
            self.info_layout = QVBoxLayout()
            self.info_layout.addWidget(QLabel(f"Nom : ???"))
            self.info_layout.addWidget(QLabel(f"Type : ???"))
            self.info_layout.addWidget(QLabel(f"Taille : ??? m"))
            self.info_layout.addWidget(QLabel(f"Poids : ??? kg"))
            self.info_layout.addWidget(QLabel(f"HP : ???"))
            self.info_layout.addWidget(QLabel(f"Génération : {self.pokemon.generation()}"))
            if self.pokemon.evolution() != None:
                self.info_layout.addWidget(QLabel(f"Evolution : ???"))
            if self.pokemon.pre_evolution() != None:
                if self.pokemon.pre_pre_evo() != None:
                    self.info_layout.addWidget(QLabel(f"Sous-évolutions : ??? et ???"))
                else: 
                    self.info_layout.addWidget(QLabel(f"Sous-évolution : ???"))
            self.info_layout.addWidget(QLabel(f"Faiblesse : ???"))
            
            self.image = QLabel()
            self.image.setPixmap(QPixmap.fromImage(img))
            self.final_layout.addLayout(self.info_layout, 0, 0)
            self.final_layout.addWidget(self.image, 0, 1)
            self.final_layout.addWidget(self.closeButton, 1, 0)
            self.setLayout(self.final_layout)
            
    def update_data(self):
        with open(BDD, encoding="utf8") as f:
            global data
            data = json.load(f)

