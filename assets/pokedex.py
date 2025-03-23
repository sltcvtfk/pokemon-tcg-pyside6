import concurrent.futures
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from assets.constante import *
from assets.pokeinfo import *
from assets.searchbar import *
import requests
import json

with open(BDD, "r",encoding="utf8") as f:
    data = json.load(f)
    
with open(POKEDEX, encoding="utf8") as f:
    res = json.load(f)
    


class addPokemon(QPushButton):
    right_click = Signal()
    left_click = Signal()

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.right_click.emit()
        elif e.button() == Qt.LeftButton:
            self.left_click.emit()

class Pokedex(QWidget): 
    def __init__(self):
        super().__init__()
        self.layout_pokedex = QGridLayout()
        self.mySearchBar = Searchbar()
        self.pages()
        self.setLayout(self.layout_pokedex)
        self.mySearchBar.lineEdit.textChanged.connect(self.update_page)
    
    @Slot()
    def pages(self):
        """Affiche les pokemons dans le pokedex"""
        self.current_page = 0
        self.pokemon_per_page = 20
        self.total_pokemon = LAST_POKEMON
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
        self.prev_button = QPushButton("Précédent")
        
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button = QPushButton("Suivant")
        self.next_button.clicked.connect(self.next_page)
        
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
        self.page_layout.addLayout(self.button_layout)
        
        self.page_widget.setLayout(self.page_layout)
        self.layout_pokedex.addWidget(self.page_widget)
        self.pokemon_layout.setContentsMargins(32, 130, 32, 32)
     
        self.update_page()
    
    def update_page(self):
        """Met à jour la page actuelle du Pokédex"""
        
        with open(BDD, "r", encoding="utf8") as f:
            global bdd
            bdd = json.load(f)
        
        for i in reversed(range(self.pokemon_layout.count())):
            self.pokemon_layout.itemAt(i).widget().setParent(None)
            
        buttons = []
        
        if self.mySearchBar.filtered == []:
            total_pokemon = self.total_pokemon
        else:
            total_pokemon = len(self.mySearchBar.filtered)
        
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
            button = addPokemon()
            button.setFixedSize(65, 65)
            button.setStyleSheet("background: transparent; border: none;") 
            button.left_click.connect(lambda poke=index: self.show_info_pokemon(poke))
            button.right_click.connect(lambda poke=index: self.show_pokemon(poke))
            self.pokemon_layout.addWidget(button, i // 4, i % 4)
            if self.mySearchBar.filtered == []:
                buttons.append((button, index))
            else:
                buttons.append((button, self.mySearchBar.filtered[index] - 1))
                        
        self.prev_button.setEnabled(self.current_page > 0)        
        self.load_pokemon_images(buttons)

    def update_pokedex_data(self):
        """Update the pokedex data"""
        with open(BDD, encoding="utf8") as file:
            global data
            data = json.load(file)
        self.update_page()
        
    def load_pokemon_images(self, buttons):
        """Load Pokemon images concurrently and set them as button icons"""
        
        def load_single_image(button, index):
            x = requests.get(res[index]["image"]["thumbnail"], stream=True)
            image = QImage()
            image.loadFromData(x.content)
            img = image.scaled(65, 65, Qt.AspectRatioMode.KeepAspectRatio)
        
            if res[index]["id"] in data["users"][data["lastConnected"]]["pokedex"]:
                img = img.convertToFormat(QImage.Format_ARGB32)
            else:
                img = img.convertToFormat(QImage.Format_Alpha8)
                
            button.setIcon(QIcon(QPixmap.fromImage(img)))
            
            button.setIconSize(QSize(60, 60))

        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(load_single_image, button, index) for button, index in buttons]
            concurrent.futures.wait(futures)
            
    def show_info_pokemon(self, index):
        """Affiche les info du pokémon sélectionné"""
        self.update_pokedex_data()
        self.pokemon = Pokeinfo(res[index]["id"])
        self.pokemon.show()
        
    def show_pokemon(self, index):
        """Fonction administrateur, elle va permettre de rajouter ou d'enlever un pokémon du pokedex"""
        if data["users"][data["lastConnected"]]["isAdmin"] == True:
            with open("json/bdd.json", "w", encoding="utf8") as file:
                
                user = data['users'][data['lastConnected']]
            
                if (int(res[index]["id"]) not in user['pokedex']):
                    user['pokedex'].append(int(res[index]["id"]))
                elif int(res[index]["id"]) in user['pokedex']:
                    user['pokedex'].remove(int(res[index]["id"]))
            
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            self.update_pokedex_data()

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
            