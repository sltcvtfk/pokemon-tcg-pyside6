from PySide6.QtGui import*
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from booster import *
from constante import *

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

class Button_Open(QPushButton):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(175, 570, 50, 50)
        self.setText("Open!")
        self.setFixedSize(50, 50)
        self.compte = 0   
        
    def click(self):
        """
        Returns:
            int: the number of times the button has been clicked
        """
        self.compte += 1
        return self.compte

class MyWindow(QMainWindow):
    def __init__(self):
        """ Va afficher la fenêtre principale de l'application en stockant les différentes 
        scènes dans un QStackedWidget, les initialisant puis 
        affichant la scène de booster par défaut.
        
        self.avoid: int: 0 if the scene is pokedex, 1 if the scene is booster
        """
        super().__init__()
        self.setGeometry(0, 0, 410, 800)
        
        self.setWindowIcon(QIcon("img/pokeball_icon.png"))
        self.setWindowTitle("Pokemon TCG")
        
        
        self.my_scenes = QStackedWidget()
        self.my_scenes.setGeometry(0, 0, 400, 700)
        self.setCentralWidget(self.my_scenes)
        
        
        
        self.avoid = 0
        
        self.scene_booster = Scene_Booster(0,0,400,700) # 0,0,400,700
        self.scene_pokedex = Scene_Pokedex(0,0,400,700)	

        self.my_scenes.addWidget(QGraphicsView(self.scene_booster))
        self.my_scenes.addWidget(QGraphicsView(self.scene_pokedex))
        
        self.init_toolbar()
        self.init_booster_scene()
        self.init_pokedex_scene()
        
        self.booster_scene()
        
    def init_pokedex_scene(self):
        """Initialise the pokedex scene
        """
        self.layout_pokedex = QGridLayout()
        self.pages()
        
        widget = QWidget()
        widget.setLayout(self.layout_pokedex)
        self.scene_pokedex.addWidget(widget)

     
            
    def init_toolbar(self):
        """Initialise the toolbar
        """
        toolbar = QToolBar("Toolbar")
        toolbar.setMovable(False)
        toolbar.setFixedHeight(75)
        toolbar.setIconSize(QSize(50, 50))
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer = QWidget()
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(right_spacer)
        self.addToolBar(Qt.BottomToolBarArea, toolbar)
        actPokedex = QAction(QIcon("img/pokedex_icon.png"), "Pokedex", self)
        actPokedex.setStatusTip("Pokedex")
        actPokedex.triggered.connect(self.pokedex_scene)
        actBooster = QAction(QIcon("img/pokeball_icon.png"), "Booster", self)
        actBooster.setStatusTip("Booster")
        actBooster.triggered.connect(self.booster_scene)
        toolbar.addSeparator()
        toolbar.addAction(actPokedex)
        toolbar.addSeparator()
        toolbar.addAction(actBooster)
        toolbar.addSeparator()
        toolbar.addWidget(left_spacer)
        
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
        if self.avoid == 1:
            self.my_scenes.setCurrentIndex(1)
        self.avoid = 0
    
    
    def booster_scene(self):
        """Change any scene to booster scene
        self.avoid: int: 0 if the scene is pokedex, 1 if the scene is booster
        """
        if self.avoid == 0:
            self.my_scenes.setCurrentIndex(0)
        self.avoid = 1


        
    
    @Slot()
    def booster_start(self):
        """Start the booster. 
        Si le compte est égal à 1, on enlève le booster, on affiche une carte
        Si le compte est égal à 6, on enlève la carte, on affiche un booster
        Sinon, on enlève la carte, on affiche une autre carte
        """
        self.open_button.click()
        print(self.open_button.compte)
        if(self.open_button.compte == 1):
            self.scene_booster.removeItem(self.boosterPixmap)
            self.carte = self.scene_booster.addPixmap(Booster().creation_carte_pokemon(random.randint(FIRST_POKEMON, LAST_POKEMON)))
            self.carte.setPos(50,50)
        elif(self.open_button.compte == 6):
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

        """Affiche les 151 premiers pokemons dans le pokedex"""
        
        self.wizard = QWizard()
        self.wizard.setWizardStyle(QWizard.AeroStyle)
        self.wizard.setStyleSheet("QWizard { background-color: #DCDCDC; }")
        # self.wizard.setOption(QWizard.NoBackButtonOnStartPage, True)
        self.wizard.setOption(QWizard.NoCancelButton, True)
        self.wizard.setOption(QWizard.HaveFinishButtonOnEarlyPages, False)  # Hide Finish button
        self.wizard.setButtonLayout([QWizard.Stretch, QWizard.BackButton, QWizard.NextButton])  # Custom button layout
        
        self.wizard.setFixedSize(375, 600)
        
        # 4 columns * 5 rows = 20 Pokemon per page
        num_pages = (809 // 20) + (1 if 809 % 20 != 0 else 0)
        
        for page_num in range(num_pages):
            page = QWizardPage()
            page.setTitle(f"Page {page_num + 1}")
            page.setStyleSheet("QWizardPage { background-color: #DCDCDC; }")
    
            layout = QGridLayout()
            layout.setSpacing(15)  # Increased spacing between items
            layout.setContentsMargins(10, 20, 10, 20)  # Adjusted margins
            
            start_index = page_num * 20
            end_index = min(start_index + 20, 809)
            
            for i, index in enumerate(range(start_index, end_index)):
                pic = QLabel()
                pic.setProperty("pokemon_index", index)
                pic.setFixedSize(65, 65)  # Slightly smaller images for better fit
                layout.addWidget(pic, i // 4, i % 4)
                
                # Add vertical spacing between rows
                if i % 4 == 0:
                    layout.setRowMinimumHeight(i // 4, 80)
            
            page.setLayout(layout)
            self.wizard.addPage(page)
        
        self.wizard.currentIdChanged.connect(self.load_pokemon_images)
        self.layout_pokedex.addWidget(self.wizard)
        self.layout_pokedex.setContentsMargins(0, 0, 0, 0)
    
    def load_pokemon_images(self, page_id):
        """Load Pokemon images for current page using concurrent requests"""
        import concurrent.futures
        
        current_page = self.wizard.page(page_id)
        current_page.setStyleSheet("QLabel { background-color: #DCDCDC ;}")
        if not current_page:
            return

        def load_single_image(widget):
            if isinstance(widget, QLabel):
                pokemon_index = widget.property("pokemon_index")
                if pokemon_index is not None:
                    try:
                        x = requests.get(res[pokemon_index]["image"]["thumbnail"], stream=True)
                        image = QImage()
                        image.loadFromData(x.content)
                        img = image.scaled(65, 65, Qt.AspectRatioMode.KeepAspectRatio)
                        widget.setPixmap(QPixmap.fromImage(img))
                    except:
                        pass

        widgets = [current_page.layout().itemAt(i).widget() 
                  for i in range(current_page.layout().count())]

        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            executor.map(load_single_image, widgets)
            
if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()



QFontDatabase.addApplicationFont("./font/GillSansStdBold.otf")



        # self.scene.addPixmap(charge_carte_image(pokemon_id))
        # self.scene.addPixmap(charge_pokemon_image(pokemon_id))
        # booster = self.scene.addPixmap(affiche_booster())
        # self.scene.removeItem(booster)
        # self.scene.items()[0].setPos(130,100)
        #self.pokemon_id = random.randint(1, 151)