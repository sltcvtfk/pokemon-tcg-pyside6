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
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer = QWidget()
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.addWidget(right_spacer)
        
        self.qactions = {
            "Pokedex": QAction(QIcon('img/pokedex_icon.png'), 'Pokedex', self),
            "Booster": QAction(QIcon('img/pokeball_icon.png'), 'Booster', self),
            "User": QAction(QIcon('img/poketrainer_icon.png'), 'User', self)
        }
        
        if data['lastConnected'] != '':
            for name, action in self.qactions:
                self.addSeparator()
                self.addAction(action)
                action.setStatusTip(name)
            self.addSeparator()
            self.addWidget(left_spacer)

        else:
            self.addSeparator()
            self.addAction(self.qactions["User"])
            self.addSeparator()
            self.addWidget(left_spacer)