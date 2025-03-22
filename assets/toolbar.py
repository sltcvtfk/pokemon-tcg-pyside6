from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from assets.constante import *
import json

with open('json/bdd.json', 'r') as file:
    data = json.load(file)

class Toolbar(QToolBar):
    def __init__(self):
        super().__init__(parent=None)
        self.setMovable(False)
        self.setFixedHeight(75)
        self.setIconSize(QSize(50, 50))
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.left_spacer = QWidget()
        self.left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_spacer = QWidget()
        self.right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        
        self.qactions = [
            QAction(QIcon('img/pokedex_icon.png'), "Pokedex", self),
            QAction(QIcon('img/pokeball_icon.png'), "Booster", self),
            QAction(QIcon('img/poketrainer_icon.png'), "Utilisateur", self)
        ]
