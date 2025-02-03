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
        
    def description(self):
        return res[self.pokedex_id-1]["description"]
        
    def height(self):
        return res[self.pokedex_id-1]["profile"]["height"]
    
    def weight(self):
        return res[self.pokedex_id-1]["profile"]["weight"]
        
    def species(self):
        return res[self.pokedex_id-1]["species"]
    
    def english_name(self):
        return res[self.pokedex_id-1]["name"]["english"]
    
    def french_name(self):
        return res[self.pokedex_id-1]["name"]["french"]
    
    def hp(self):
        return res[self.pokedex_id-1]["base"]["HP"]
    
    def description(self): 
        return res[self.pokedex_id-1]["description"]
    
    def his_type(self):
        return TYPE_DICT[res[self.pokedex_id-1]["type"][0]]
    
    def weakness(self):
        return WEAKNESS_TYPE_DICT[TYPE_DICT[res[self.pokedex_id-1]["type"][0]]]
    
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
        
    def load_carte_image(self, pokedex_id: int):
        with open(CARTE_DICT[res[pokedex_id-1]["type"][0]], 'rb') as image:
            img = QImage()
            img.loadFromData(image.read())
            img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
            return img

    def load_pokemon_image(self, pokedex_id: int):
        x = requests.get(res[pokedex_id-1]["image"]["hires"], stream=True)
        image = QImage()
        image.loadFromData(x.content)
        img = image.scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio)
        return img
    
    def load_pokemon_weakness_retreat_image(self, pokedex_id: int):
        with open(WEAKNESS_IMAGE_DICT[TYPE_DICT[res[pokedex_id-1]["type"][0]]], 'rb') as image:
            weakness = QImage()
            weakness.loadFromData(image.read())
            weakness = weakness.scaled(13, 13, Qt.AspectRatioMode.KeepAspectRatio)
        with open("img/type/Normal.png", 'rb') as image:
            retreat = QImage()
            retreat.loadFromData(image.read())
            retreat = retreat.scaled(13, 13, Qt.AspectRatioMode.KeepAspectRatio)
        return weakness, retreat
        
    

    def creation_carte_pokemon(self, pokedex_id: int):
        carte = self.load_carte_image(pokedex_id)
        new_pokemon = self.load_pokemon_image(pokedex_id)
        weakness_retreat = self.load_pokemon_weakness_retreat_image(pokedex_id)
        my_pokemon = Pokemon(pokedex_id)
        # Assembler les deux images
        painter = QPainter(carte)
        painter.drawImage(90, 50, new_pokemon)
        painter.setFont(HP_FONT)
        painter.drawText(50, 210, f"N°{pokedex_id:04d} {my_pokemon.species()} HT: {my_pokemon.height()} WT: {my_pokemon.weight()} ") 

        if my_pokemon.his_type() == "Dark":
            painter.setPen(Qt.white)
        else:
            painter.setPen(Qt.black)
            
        if my_pokemon.hp() >= 100:
            painter.drawText(213, 30, "HP")
            painter.setFont(GILL_SANS_FONT)
            painter.drawText(225, 30, str(my_pokemon.hp()))
        else:
            painter.drawText(223, 30, "HP")
            painter.setFont(GILL_SANS_FONT)
            painter.drawText(237, 30, str(my_pokemon.hp()))

        painter.drawText(55, 30, my_pokemon.french_name())
        
        #painter.drawText(55, 40, my_pokemon.description())
        
        painter.drawImage(75, 362, weakness_retreat[0])
        painter.drawImage(195, 362, weakness_retreat[1])
    
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
        
    # def start_booster(self):
    #     for i in range(6):
    #         self.add_to_list()
    #     return self.pokemon  
    
        
# def start_booster():

