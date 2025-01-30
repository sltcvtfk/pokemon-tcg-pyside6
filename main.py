from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QMainWindow, QWidget ,QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QBrush, QPen, QColor, QCloseEvent, QPainter, QPaintEvent, QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem
)
from PySide6.QtCore import Qt
from booster import *

#class Pokemon(): 

        

class Bouton(QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        

class Scene(QGraphicsScene):
    def __init__(self, *args): 
        super().__init__(*args)
        self.rect = QGraphicsRectItem(0, 0, 375, 680)
        self.rect.setPos(10, 10)
        brush = QBrush(QColor(220,220,220))
        self.rect.setBrush(brush)
        pen = QPen(QColor(0,0,0))
        pen.setWidth(1)
        self.rect.setPen(pen)
        self.addItem(self.rect)
        
    #def setColor(self, *args):
     #   brush = QBrush(QColor())
    
    

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.scene = Scene(0,0,400,700)
        
        # self.scene.addPixmap(charge_carte_image(pokemon_id))
        # self.scene.addPixmap(charge_pokemon_image(pokemon_id))
        booster = self.scene.addPixmap(affiche_booster())
        self.scene.items()[0].setPos(60,50)
        # self.scene.removeItem(booster)
        # self.scene.items()[0].setPos(130,100)
        view = QGraphicsView(self.scene)
        self.layout = QHBoxLayout()
        self.open_button = QPushButton("Open!")
        self.open_button.setFixedSize(50, 50)
        self.open_button.setGeometry(175, 570, 50, 50)
        self.open_button.clicked.connect(start_booster)
        self.scene.addWidget(self.open_button)
        
        
        
        self.layout.addWidget(view)
      
        
        centralWidget.setLayout(self.layout)





app = QApplication()

myWindow = MyWindow()

myWindow.show()
app.exec()

