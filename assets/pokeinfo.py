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
        self.update_data()
        self.pokemon = Pokemon(pokedex_id)
        userConnected = data["users"][data["lastConnected"]]["pokedex"]
        self.french_name = f"{self.pokemon.french_name()} ({self.pokemon.pokedex_id})" if pokedex_id in userConnected else "???";
        self.type = f"{self.pokemon.his_type()}" if pokedex_id in userConnected else "???";
        self.hgt = f"{self.pokemon.height()}" if pokedex_id in userConnected else "??? m";
        self.wgt = f"{self.pokemon.weight()}" if pokedex_id in userConnected else "??? kg";
        self.hp = f"{self.pokemon.hp()}" if pokedex_id in userConnected else "???";
        self.gen = f"{self.pokemon.generation()}"
        self.weakness = f"Type {ENGLISH_TYPE_TO_FRENCH_DICT[self.pokemon.weakness()].lower()}" if pokedex_id in userConnected else "???"
                
        self.setWindowTitle(self.pokemon.french_name())
        x = requests.get(self.pokemon.image_links()["thumbnail"], stream=True)
        image = QImage()
        image.loadFromData(x.content)
        image.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio)
        img = image if pokedex_id in userConnected else image.convertToFormat(QImage.Format_Alpha8)
        self.setWindowIcon(QIcon(QPixmap().fromImage(img)))
        self.closeButton = QPushButton("Fermer")
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setStyleSheet("QPushButton { border: 1px solid #bc545c; border-radius: 3px; text-align: center; background-color: #ebe8e8; } QPushButton:hover { background-color: #d6d6d6; } QPushButton:disabled { background-color: #7d7d7d; color: black; }")
        self.final_layout = QGridLayout()
        self.info_layout = QVBoxLayout()
        self.info_layout.addWidget(QLabel(f"Nom : {self.french_name}"))
        self.info_layout.addWidget(QLabel(f"Type : {self.type}"))
        self.info_layout.addWidget(QLabel(f"Taille : {self.hgt}"))
        self.info_layout.addWidget(QLabel(f"Poids : {self.wgt}"))
        self.info_layout.addWidget(QLabel(f"HP : {self.hp}"))
        self.info_layout.addWidget(QLabel(f"Génération : {self.gen}"))
        if self.pokemon.evolution() != None:
            self.evo = f"{Pokemon(self.pokemon.evolution()).french_name()}" if Pokemon(int(self.pokemon.evolution())).pokedex_id in userConnected else "???"
            self.info_layout.addWidget(QLabel(f"Evolution : {self.evo}"))
        if self.pokemon.pre_evolution() != None:
            self.pre_evo = f"{Pokemon(int(self.pokemon.pre_evolution())).french_name()}" if Pokemon(int(self.pokemon.pre_evolution())).pokedex_id in userConnected else "???"  
            if self.pokemon.pre_pre_evo() != None:
                self.pre_pre_evo = f"{Pokemon(int(self.pokemon.pre_pre_evo())).french_name()}" if Pokemon(int(self.pokemon.pre_pre_evo())).pokedex_id in userConnected else "???"  
                self.info_layout.addWidget(QLabel(f"Sous-évolutions : {self.pre_pre_evo} et {self.pre_evo} "))
            else: 
                self.info_layout.addWidget(QLabel(f"Sous-évolution : {self.pre_evo}"))
        self.info_layout.addWidget(QLabel(f"Faiblesse : {self.weakness}"))
        self.info_layout.addWidget(self.closeButton, alignment=Qt.AlignBottom | Qt.AlignRight)
        self.image = QLabel()
        self.image.setPixmap(QPixmap.fromImage(img))
        
        self.final_layout.addLayout(self.info_layout, 0, 0)
        self.final_layout.addWidget(self.image, 0, 1)
        self.setLayout(self.final_layout)
            
    def update_data(self):
        with open(BDD, encoding="utf8") as f:
            global data
            data = json.load(f)

