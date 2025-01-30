from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QMainWindow, QWidget ,QHBoxLayout, QPushButton, QLabel, QGridLayout
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
from searchbar import Searchbar

with open('pokedex.json', encoding="utf8") as f:
    res = json.load(f)

x = requests.get(res[0]["image"]["hires"], stream=True)

class Label_image(QLabel):
    def __init__(self):
        super().__init__()
        image = QImage()
        image.loadFromData(x.text)
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap)

class Scene(QGraphicsScene):
    def __init__(self, *args): 
        super().__init__(*args)
        self.rect = QGraphicsRectItem(0, 0, 300, 475)
        
        self.rect.setPos(10, 10)
        brush = QBrush(QColor(220,220,220))
        self.rect.setBrush(brush)
        pen = QPen(QColor(0,0,0))
        pen.setWidth(1)
        self.rect.setPen(pen)
        self.addItem(self.rect)

    
    

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.scene = Scene(0,0,325,500)
        view = QGraphicsView(self.scene)
        
        self.searchBar = Searchbar()
        self.searchBar.setFixedWidth(200)
        
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(view)
        self.layout.addWidget(self.searchBar)
        
        centralWidget.setLayout(self.layout)

app = QApplication()

myWindow = MyWindow()

myWindow.resize(800, 600)


myWindow.show()
app.exec()