import random
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from assets.booster import *
from assets.constante import *
from assets.login import *
from assets.toolbar import Toolbar
from assets.pokeinfo import Pokeinfo
from assets.pokedex import Pokedex

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
        
class Scene_Logged(QGraphicsScene) :
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
        self.setText("Ouvrir!")
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
        # Adapte la scène à la taille de l'écran (à finir peut être)
        # screen_size = app.primaryScreen().availableGeometry()
        # (self.screen_width, self.screen_height) = (screen_size.width(), screen_size.height())
        
        # self.setGeometry(0, 0, round(self.screen_width/4.7), round(self.screen_height/1.35))
        
        self.setGeometry(0, 0, 410, 800)
        
        self.setWindowIcon(QIcon("img/pokeball_icon.png"))
        self.setWindowTitle("Pokémon TCG")
        
        
        self.my_scenes = QStackedWidget()
        self.my_scenes.setGeometry(0, 0, 400, 700)
        self.setCentralWidget(self.my_scenes)
        
        self.scene_booster = Scene_Booster(0,0,400,700) # 0,0,400,700
        self.scene_pokedex = Scene_Pokedex(0,0,400,700)	
        self.scene_connexion = Scene_Connexion(0 ,0 ,400, 700)
        self.scene_logged = Scene_Logged(0,0,400,700)

        self.my_scenes.addWidget(QGraphicsView(self.scene_booster))
        self.my_scenes.addWidget(QGraphicsView(self.scene_pokedex))
        self.my_scenes.addWidget(QGraphicsView(self.scene_connexion))
        self.my_scenes.addWidget(QGraphicsView(self.scene_logged))
        
        self.init_toolbar()
        self.init_booster_scene()
        self.init_pokedex_scene()
        self.init_connexion_scene()
        self.init_logged_scene()
        
        user = User();
        
        if user.username != "":
            self.booster_scene()
        else:
            self.connexion_scene()
        
    def init_pokedex_scene(self):
        """Initialise the pokedex scene
        """
        self.pokedex = Pokedex()
        self.scene_pokedex.addWidget(self.pokedex)
        self.scene_pokedex.addWidget(self.pokedex.mySearchBar)
    
    def update_bdd(self):
        """Met à jour la base de données
        """
        with open(BDD, encoding="utf8") as file:
            json.load(file)

    def init_connexion_scene(self) :
        """Initialise la scène de connexion
        """
        
        self.connexion = Connexion()
        self.connexion.setFixedSize(400, 700)
        self.connexion.loginButton.clicked.connect(self.connexion_scene)
        self.scene_connexion.addWidget(self.connexion)
        
    def init_logged_scene(self) :
        """Initialise la scène d'utilisateur connecté
        """
        self.logged = Logged()
        self.logged.setFixedSize(400, 700)
    
        self.logged.disconnectButton.clicked.connect(self.connexion_scene)

        self.scene_logged.addWidget(self.logged)
        
    def init_toolbar(self):
        """Initialise la Toolbar
        """
        
        with open(BDD, "r", encoding="utf8") as f:
            global bdd
            bdd = json.load(f)
            
        self.toolbar = Toolbar()

        self.toolbar.addWidget(self.toolbar.right_spacer)
        for action in self.toolbar.qactions:
            self.toolbar.addAction(action)
        
        
        self.toolbar.qactions[0].triggered.connect(self.pokedex_scene)
        self.toolbar.qactions[1].triggered.connect(self.booster_scene)
        self.toolbar.qactions[2].triggered.connect(self.connexion_scene)

        # print(bdd['lastConnected'])
        if bdd['lastConnected'] == "":
            self.toolbar.removeAction(self.toolbar.actions()[1])
            self.toolbar.removeAction(self.toolbar.actions()[1])
        
        
        self.toolbar.addWidget(self.toolbar.left_spacer)
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)
        
    
    def update_toolbar(self):
        """Met à jour la Toolbar
        """
        self.removeToolBar(self.toolbar)
        self.update_bdd()
        self.init_toolbar()
        
        

    
    def init_booster_scene(self):
        """Initialise la scène de booster
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
        """Change n'importe quelle scène en scène de pokedex
        """
        self.pokedex.update_pokedex_data()
        self.my_scenes.setCurrentIndex(1)
    
    def booster_scene(self):
        """Change n'importe quelle scène en scène de booster
        """
        self.my_scenes.setCurrentIndex(0)
 
    def connexion_scene(self):
        """Change n'importe quelle scène en scène de connexion
        """
        
        with open(BDD, "r", encoding="utf8") as f:
            global bdd
            bdd = json.load(f)
        
        if (self.logged.disconnectButton.clicked) or (bdd['lastConnected'] == "" ):  
            self.update_toolbar()
            self.repaint()
            self.my_scenes.setCurrentIndex(2)
        if (self.connexion.loginButton.clicked.connect(self.connexion.verifLogin) == True) or (bdd['lastConnected'] != ""): 
            self.update_toolbar()
            self.my_scenes.setCurrentIndex(3)


    @Slot()
    def booster_start(self):
        
        """Lance le booster. 
        Si le compte est égal à 1, on enlève le booster, on affiche une carte
        Si le compte est égal à 6, on enlève la carte, on affiche un booster
        Sinon, on enlève la carte, on affiche une autre carte
        """
        self.open_button._click()

        
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

if __name__ == "__main__":
    app = QApplication([])


    win = MyWindow()
    win.show()
    
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    win.move(center - win.rect().center())
    
    app.exec()



QFontDatabase.addApplicationFont("./font/GillSansStdBold.otf") # Ajoute la police d'écriture à la base de données des polices sur QT



