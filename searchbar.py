from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QMainWindow, QWidget ,QHBoxLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QBrush, QPen, QColor, QCloseEvent, QPainter, QPaintEvent, QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsItem
)
from PySide6.QtNetwork import (QNetworkAccessManager )
import requests
import json



class Searchbar(QWidget) :
    """ Barre de recherche
    Args:
        QWidget
    """
    
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        #search bar initialisation
        self.label = QLabel()
        self.closeButton = QPushButton()
        self.buttons = []
        
        
        self.initUI()
        
    def initUI(self) :
        """ Initialisation de l'interface utilisateur de la barre de recherche
        """
        
        #initialisation des Widgets
        self.lineEdit = QLineEdit()
        self.searchButton = QPushButton()
        
        
        self.buttons.append(self.closeButton)
        self.buttons.append(self.searchButton)
        
        #création du layout
        layout = QHBoxLayout
        layout.addWidget(self.searchButton)
        layout.addWidget(self.lineEdit)