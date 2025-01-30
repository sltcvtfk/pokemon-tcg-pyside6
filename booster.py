from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt

import requests
import json
import random

carte_dict = {
    "Fighting": "img/Fighting.png",
    "Dragon": "img/Dragon.png",
    "Water": "img/Water.png",
    "Electric": "img/Electric.png",
    "Fire": "img/Fire.png",
    "Dark": "img/Dark.png",
    "Water": "img/Water.png",
    "Grass": "img/Grass.png",
    "Normal": "img/Normal.png",
    "Steel": "img/Steel.png",
    "Poison": "img/Grass.png",
    "Ice": "img/Water.png",
    "Rock": "img/Fighting.png",
    "Ground": "img/Fighting.png",
    "Fairy": "img/Psychic.png",
    "Flying": "img/Normal.png",
    "Bug": "img/Grass.png",
    "Ghost": "img/Psychic.png",
}

with open('pokedex.json', encoding="utf8") as f:
    res = json.load(f)
    
def charge_carte_image(pokedex_id: int):
    with open(carte_dict[res[pokedex_id-1]["type"][0]], 'rb') as image:
        img = QImage()
        img.loadFromData(image.read())
        img = img.scaled(300, 560, Qt.AspectRatioMode.KeepAspectRatio)
        return img

def charge_pokemon_image(pokedex_id: int):
    x = requests.get(res[pokedex_id-1]["image"]["hires"], stream=True)
    image = QImage()
    image.loadFromData(x.content)
    img = image.scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio)
    return img

def assemble_carte_pokemon(pokedex_id: int):
    carte = charge_carte_image(pokedex_id)
    pokemon = charge_pokemon_image(pokedex_id)
    
    # Assembler les deux images
    painter = QPainter(carte)
    painter.drawImage(60, 50, pokemon)  # Ajustez les coordonnées selon vos besoins
    painter.end()
    
    pixmap = QPixmap.fromImage(carte)
    return pixmap

def affiche_booster():
    with open("img/booster.png", 'rb') as image:
        img = QImage()
        img.loadFromData(image.read())
        img = img.scaled(300, 510, Qt.AspectRatioMode.KeepAspectRatio)
        pixmap = QPixmap.fromImage(img)
        return pixmap
    
# def start_booster():
    
    