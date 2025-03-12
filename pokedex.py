from PySide6.QtGui import *
from PySide6.QtCore import Qt
from constante import *
import json
import requests

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    
i = 1
while (i <= LAST_POKEMON):
    x = requests.get(res[i-1]["image"]["thumbnail"], stream=True)
    image = QImage()
    i += 1