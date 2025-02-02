from PySide6.QtGui import *
from PySide6.QtCore import Qt

import requests
import json
import random
from constante import *

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    
class Pokemon(): 
    def __init__(self, pokedex_id):
        self.pokedex_id = pokedex_id
        
    def english_name(self):
        return res[self.pokedex_id-1]["name"]["english"]
    
    def french_name(self):
        return res[self.pokedex_id-1]["name"]["french"]
    
    def hp(self):
        return res[self.pokedex_id-1]["base"]["HP"]
    
    def description(self): 
        return res[self.pokedex_id-1]["description"]
    
    def his_type(self):
        return res[self.pokedex_id-1]["type"][0]
    
    def weakness(self):
        return WEAKNESS_DICT[res[self.pokedex_id-1]["type"][0]]
    
    def generation(self):
        for i, (start, end) in enumerate(GENERATION):
            if self.pokedex_id >= start and self.pokedex_id <= end:
                return i+1
    def __repr__(self):
        return f"{self.english_name()} ({self.french_name()})\nPV: {self.hp()}\nType: {self.his_type()}\nWeakness: {self.weakness()}\nGeneration: {self.generation()}"
      


class Booster():
    def __init__(self):
        self.pokemon = []
        
    def add_to_list(self, pokedex_id):
        self.pokemon.append(Pokemon(pokedex_id))
        
    def charge_carte_image(self, pokedex_id: int):
        with open(CARTE_DICT[res[pokedex_id-1]["type"][0]], 'rb') as image:
            img = QImage()
            img.loadFromData(image.read())
            img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
            return img

    def charge_pokemon_image(self, pokedex_id: int):
        x = requests.get(res[pokedex_id-1]["image"]["hires"], stream=True)
        image = QImage()
        image.loadFromData(x.content)
        img = image.scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio)
        return img

    def assemble_carte_pokemon(self, pokedex_id: int):
        carte = self.charge_carte_image(pokedex_id)
        new_pokemon = self.charge_pokemon_image(pokedex_id)
        # Assembler les deux images
        painter = QPainter(carte)
        painter.drawImage(70, 50, new_pokemon)
        # Ajustez les coordonnées selon vos besoins
        painter.end()
        
        pixmap = QPixmap.fromImage(carte)
        return pixmap
    
    def affiche_booster(self):
        with open(BOOSTER, 'rb') as image:
            img = QImage()
            img.loadFromData(image.read())
            img = img.scaled(300, 510, Qt.AspectRatioMode.KeepAspectRatio)
            pixmap = QPixmap.fromImage(img)
            return pixmap
    
        
# def start_booster():

