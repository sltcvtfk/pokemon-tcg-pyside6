from PySide6.QtGui import *
from PySide6.QtCore import Qt

import requests
import json

from assets.constante import *

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    
class Pokemon(): 
    def __init__(self, pokedex_id: int):
        """

        Args:
            pokedex_id (int): Pokedex ID of the pokemon
        """
        self.pokedex_id = pokedex_id
        
    def height(self):
        """
            Returns:
                int: Height of the pokemon
        """
        return res[self.pokedex_id-1]["profile"]["height"]
    
    def weight(self):
        """
            Returns:
                int: Weight of the pokemon
        """
        
        return res[self.pokedex_id-1]["profile"]["weight"]
        
    def species(self):
        """
            Returns:
                str: Species of the pokemon
        """
        return res[self.pokedex_id-1]["species"]
    
    def english_name(self):
        """
            Returns:
                str: English name of the pokemon
        """
        return res[self.pokedex_id-1]["name"]["english"]

    def french_name(self):
        """
            Returns:
                str: French name of the pokemon
        """
        return res[self.pokedex_id-1]["name"]["french"]
    
    def hp(self):
        """
        Returns:
            int: HP of the pokemon
        """
        return res[self.pokedex_id-1]["base"]["HP"]
    
    def description(self): 
        """
            Returns:
                str: Description of the pokemon
        """
        return res[self.pokedex_id-1]["description"]
    
    def his_type(self):
        """
            Returns:
                str: Type of the pokemon
        """
        return TYPE_DICT[res[self.pokedex_id-1]["type"][0]]
    
    def weakness(self):
        """
        Returns:
            str: Weakness of the pokemon
        """
        return WEAKNESS_TYPE_DICT[TYPE_DICT[res[self.pokedex_id-1]["type"][0]]]
    
    def generation(self):
        """
            Returns:
                int: Generation of the pokemon
        """
        for i, (start, end) in enumerate(GENERATION):
            if self.pokedex_id >= start and self.pokedex_id <= end:
                return i+1     
    
    def has_prev_evolution(self):
        """ 
            Returns: 
                bool: True if the pokemon has a previous evolution
        """
        if len(res[self.pokedex_id-1]["evolution"]) != 0:
            if "prev" in res[self.pokedex_id-1]["evolution"]:
                return True
        return False
    
    def prev_evolution(self):
        """
            Returns:
                int: Pokedex ID of the previous evolution
        """
        return int(res[self.pokedex_id-1]["evolution"]["prev"][0])
        
    def prev_evo_has_prev_evo(self):
        """ 
            Returns: 
                bool: True if the previous evolution has a previous evolution
        """
        prev = self.prev_evolution()
        if "prev" in res[prev-1]["evolution"]:
            return True
        return False
        
    def __repr__(self):
        return f"{self.english_name()} ({self.french_name()})\nPV: {self.hp()}\nType: {self.his_type()}\nWeakness: {self.weakness()}\nGeneration: {self.generation()}"


class Booster():
    def __init__(self):
        self.pokemons = []
        
    def add_to_list(self, pokedex_id):
        self.pokemons.append(Pokemon(pokedex_id))
        
    def load_carte_image(self, pokedex_id: int, how_many_prev: int):
        """
            Returns:
                QImage: Image of the card
        """
        
        if how_many_prev == 0:
            with open(BASIC_CARD_DICT[res[pokedex_id-1]["type"][0]], 'rb') as image:
                img = QImage()
                img.loadFromData(image.read())
                img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
                return img
        elif how_many_prev == 1:
            with open(STAGE1_CARD_DICT[res[pokedex_id-1]["type"][0]], 'rb') as image:
                img = QImage()
                img.loadFromData(image.read())
                img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
                return img
        elif how_many_prev == 2:
            with open(STAGE2_CARD_DICT[res[pokedex_id-1]["type"][0]], 'rb') as image:
                img = QImage()
                img.loadFromData(image.read())
                img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
                return img

    def load_pokemon_image(self, pokedex_id: int):
        """
            Returns:
                QImage: Image of the pokemon
        """
        x = requests.get(res[pokedex_id-1]["image"]["hires"], stream=True)
        image = QImage()
        image.loadFromData(x.content)
        img = image.scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio)
        return img
    
    def load_prev_evolution_image(self, pokemon: Pokemon):
        """
            Returns:
                QImage: Image of the previous evolution
        """
        self.prev = pokemon.prev_evolution()
        if self.prev != None:
            x = requests.get(res[self.prev-1]["image"]["sprite"], stream=True)
            image = QImage()
            image.loadFromData(x.content)
            img = image.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio)
            return img
    
    def load_pokemon_weakness_retreat_image(self, pokedex_id: int):
        """
            Returns:
                tuple: Images of the weakness and retreat
        """
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
        """
            Returns:
                QPixmap: Image of the card with the pokemon, its previous evolution, its weakness and retreat, its HP, its name, its height and weight and its species
        """
        
        my_pokemon = Pokemon(pokedex_id)
        
        if my_pokemon.has_prev_evolution():
            if my_pokemon.prev_evo_has_prev_evo():
                carte = self.load_carte_image(pokedex_id, 2)
            else:
                carte = self.load_carte_image(pokedex_id, 1)
            self.prev_evo_image = self.load_prev_evolution_image(my_pokemon)
            self.prev_evo = res[my_pokemon.prev_evolution()-1]["name"]["french"]
        else:
            carte = self.load_carte_image(pokedex_id, 0)
            self.prev_evo = None

        new_pokemon = self.load_pokemon_image(pokedex_id)
        weakness_retreat = self.load_pokemon_weakness_retreat_image(pokedex_id)
        
        # Assembler les deux images
        painter = QPainter(carte)
        painter.drawImage(85, 60, new_pokemon)
        painter.setFont(EVOLUTION_FONT)
        if self.prev_evo != None:
            painter.drawImage(10, 27, self.prev_evo_image)
            painter.drawText(50, 45, f"Evolution de : {self.prev_evo}")    
            
        painter.setFont(HP_FONT)
        painter.drawText(50, 210, f"N°{pokedex_id:03d} {my_pokemon.species()} HT: {my_pokemon.height()} WT: {my_pokemon.weight()} ") 
        

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
        """
            Returns:
                QPixmap: Image of the booster
        """
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

