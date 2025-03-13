import random
import concurrent.futures
from PySide6.QtGui import*
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from assets.booster import *
from assets.constante import *
from assets.searchbar import *
from assets.login import *
from assets.toolbar import Toolbar

with open(BDD, "r",encoding="utf8") as f:
    data = json.load(f)

with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)

class Bouton(QPushButton):
    def __init__(self, parent=None):
        super().__init__()


class Scene_Booster(QGraphicsScene):
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
        
class Scene_Pokedex(QGraphicsScene):
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
        
class Scene_Connexion(QGraphicsScene) :
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
        
class Button_Open(QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(175, 570, 50, 50)
        self.setText("Open!")
        self.setFixedSize(50, 50)
        self.compte = 0   
        
    def _click(self):
        """
        Returns:
            int: the number of times the button has been clicked
        """
        self.compte += 1
        return self.compte

class MyWindow(QMainWindow):
    def __init__(self):
        """ Hérite de QMainWindow
        
        Va afficher la fenêtre principale de l'application en stockant les différentes 
        scènes dans un QStackedWidget, les initialisant puis 
        affichant la scène de booster par défaut.
        
        """
        super().__init__()
        self.setGeometry(0, 0, 410, 800)
        
        self.setWindowIcon(QIcon("img/pokeball_icon.png"))
        self.setWindowTitle("Pokémon TCG")
        
        
        self.my_scenes = QStackedWidget()
        self.my_scenes.setGeometry(0, 0, 400, 700)
        self.setCentralWidget(self.my_scenes)
        self.searchBar = Searchbar()
        
        self.scene_booster = Scene_Booster(0,0,400,700) # 0,0,400,700
        self.scene_pokedex = Scene_Pokedex(0,0,400,700)	
        self.scene_connexion = Scene_Connexion(0 ,0 ,400, 700)

        self.my_scenes.addWidget(QGraphicsView(self.scene_booster))
        self.my_scenes.addWidget(QGraphicsView(self.scene_pokedex))
        self.my_scenes.addWidget(QGraphicsView(self.scene_connexion))
        
        self.init_toolbar()
        self.init_booster_scene()
        self.init_pokedex_scene()
        self.init_connexion_scene()
        
        if data['lastConnected'] != "":
            self.booster_scene()
        else:
            self.connexion_scene()
        
    def init_pokedex_scene(self):
        """Initialise the pokedex scene
        """
        self.layout_pokedex = QGridLayout()
        self.pages()
        
        widget = QWidget()
        widget.setLayout(self.layout_pokedex)
        self.scene_pokedex.addWidget(widget)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(QGraphicsView(self.scene_pokedex))
        self.scene_pokedex.addWidget(self.searchBar)
        self.searchBar.lineEdit.textChanged.connect(self.update_page)
        
        widget.setLayout(self.layout)


    def init_connexion_scene(self) :
        """Initialise la scène de connexion
        """
        
        self.connexion = Connexion()
        self.connexion.setFixedSize(400, 700)
        self.scene_connexion.addWidget(self.connexion)
            
    def init_toolbar(self):
        """Initialise the toolbar
        """
        
        self.toolbar = Toolbar()
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)
    
        self.toolbar.qactions["Pokedex"].triggered.connect(self.pokedex_scene)
        self.toolbar.qactions["Booster"].triggered.connect(self.booster_scene)
        self.toolbar.qactions["User"].triggered.connect(self.connexion_scene)

        
    def init_booster_scene(self):
        """Initialise the booster scene
        """
        self.open_button = Button_Open()
        self.open_button.setFixedSize(50, 50)
        self.open_button.setGeometry(175, 570, 50, 50)


        self.booster = Booster()
        self.boosterPixmap = self.scene_booster.addPixmap(self.booster.affiche_booster())
        self.boosterPixmap.setPos(60,50)
        
        self.open_button.clicked.connect(self.booster_start)
        self.scene_booster.addWidget(self.open_button)      
        
        
    def pokedex_scene(self):
        """Change any scene to pokedex scene
        """
        self.my_scenes.setCurrentIndex(1)
    
    def booster_scene(self):
        """Change any scene to booster scene
        """
        self.my_scenes.setCurrentIndex(0)
 
    def connexion_scene(self):
        """Change any scene to booster scene
        """
        self.my_scenes.setCurrentIndex(2)

    @Slot()
    def booster_start(self):
        
        """Start the booster. 
        Si le compte est égal à 1, on enlève le booster, on affiche une carte
        Si le compte est égal à 6, on enlève la carte, on affiche un booster
        Sinon, on enlève la carte, on affiche une autre carte
        """
        
        self.open_button._click()
        
        
        # print(self.open_button.compte)
        
        if (self.open_button.compte == 1):
            self.scene_booster.removeItem(self.boosterPixmap)
            self.carte = self.scene_booster.addPixmap(Booster().creation_carte_pokemon(random.randint(FIRST_POKEMON, LAST_POKEMON)))
            self.carte.setPos(50,50)
            
        elif (self.open_button.compte == 6):
            self.open_button.compte = 0
            self.scene_booster.removeItem(self.carte)
            self.boosterPixmap = self.scene_booster.addPixmap(Booster().affiche_booster())
            self.boosterPixmap.setPos(60,50)
            
        else:
            self.scene_booster.removeItem(self.carte)
            self.carte = self.scene_booster.addPixmap(Booster().creation_carte_pokemon(random.randint(FIRST_POKEMON, LAST_POKEMON)))
            self.carte.setPos(50,50)
            
    @Slot()
    def pages(self):
        """Affiche les pokemons dans le pokedex"""
        self.current_page = 0
        self.pokemon_per_page = 20
        self.total_pokemon = 809
        self.num_pages = (LAST_POKEMON // self.pokemon_per_page) + (1 if LAST_POKEMON % self.pokemon_per_page != 0 else 0)
        
        self.page_widget = QWidget()
        self.page_widget.setObjectName("page_widget")
        self.page_widget.setStyleSheet("QWidget#page_widget { border-image: url(./img/motisma_dex.png);}")
        
        self.page_widget.setFixedSize(375, 682)
        self.page_layout = QVBoxLayout()
        self.pokemon_layout = QGridLayout()

        self.page_layout.addLayout(self.pokemon_layout)
        
        self.button_layout = QHBoxLayout()
        self.button_layout.setContentsMargins(32, 0, 32, 120)
        self.prev_button = QPushButton("Previous")
        
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_page)
        
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.page_layout.addLayout(self.button_layout)
        
        self.page_widget.setLayout(self.page_layout)
        self.layout_pokedex.addWidget(self.page_widget)
        self.pokemon_layout.setContentsMargins(32, 130, 32, 32)
     
        self.update_page()
        
    # def update_page(self):
    #     """Met à jour la page actuelle du pokedex"""
    #     for i in reversed(range(self.pokemon_layout.count())):
    #         self.pokemon_layout.itemAt(i).widget().setParent(None)
        
    #     labels = []
    #     for i in range(self.pokemon_per_page):
    #         index = self.current_page * self.pokemon_per_page + i
    #         if index >= self.total_pokemon:
    #             break
    #         pic = QLabel()
    #         pic.setFixedSize(65, 65)
    #         self.pokemon_layout.addWidget(pic, i // 4, i % 4)
    #         labels.append((pic, index))
        
    #     self.prev_button.setEnabled(self.current_page > 0)
    #     self.next_button.setEnabled(self.current_page < self.num_pages - 1)
        
    #     self.load_pokemon_images(labels)
        
    def update_page(self):
        """Met à jour la page actuelle du Pokédex"""
        
        for i in reversed(range(self.pokemon_layout.count())):
            self.pokemon_layout.itemAt(i).widget().setParent(None)
            
        labels = []
        
        if self.searchBar.filtered == []:
            total_pokemon = self.total_pokemon
        else:
            total_pokemon = len(self.searchBar.filtered)
        
        self.last_page = (total_pokemon // self.pokemon_per_page) + (1 if total_pokemon % self.pokemon_per_page != 0 else 0) - 1
        
        if self.current_page >= self.last_page:
            self.current_page = self.last_page
        
        for i in range(self.pokemon_per_page):
            index = self.current_page * self.pokemon_per_page + i
            if index >= total_pokemon:
                self.next_button.setDisabled(index >= total_pokemon)
                break
            else:
                self.next_button.setEnabled(self.current_page < self.last_page)
            pic = QLabel()
            pic.setFixedSize(65, 65)
            self.pokemon_layout.addWidget(pic, i // 4, i % 4)
            if self.searchBar.filtered == []:
                labels.append((pic, index))
            else:
                labels.append((pic, self.searchBar.filtered[index] - 1))
                        
        self.prev_button.setEnabled(self.current_page > 0)        
        self.load_pokemon_images(labels)
    
    def load_pokemon_images(self, labels):
        """Load Pokemon images concurrently"""
        
        def load_single_image(label, index):
            x = requests.get(res[index]["image"]["thumbnail"], stream=True)
            image = QImage()
            image.loadFromData(x.content)
            img = image.scaled(65, 65, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(QPixmap.fromImage(img))

        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(load_single_image, label, index) for label, index in labels]
            concurrent.futures.wait(futures)

    
    def prev_page(self):
        """Go to the previous page"""
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page()
    
    def next_page(self):
        """Go to the next page"""
        if self.current_page < self.num_pages - 1:
            self.current_page += 1
            self.update_page()
            
if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()



QFontDatabase.addApplicationFont("./font/GillSansStdBold.otf") # Ajoute la police d'écriture à la base de données des polices sur QT



        # self.scene.addPixmap(charge_carte_image(pokemon_id))
        # self.scene.addPixmap(charge_pokemon_image(pokemon_id))
        # booster = self.scene.addPixmap(affiche_booster())
        # self.scene.removeItem(booster)
        # self.scene.items()[0].setPos(130,100)
        #self.pokemon_id = random.randint(1, 151)