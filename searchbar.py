from PySide6.QtWidgets import  QWidget , QLabel, QLineEdit, QVBoxLayout

import json

TYPES = { "eau" : "water",
    "feu" : "fire",
    "plante" : "grass",
    "combat" : "fighting",
    "normal" : "normal",
    "glace" : "ice",
    "insecte" : "bug",
    "poison" : "poison",
    "dragon" : "dragon",
    "acier" : "steel",
    "psy" : "psychic",
    "sol" : "ground",
    "ténèbres" : "dark",
    "roche" : "rock",
    "spectre" : "ghost",
    "fée" : "fairy",
    "vol" : "flying",
    "électrik" : "electric"
}

class Searchbar(QWidget) :
    """ Barre de recherche
    Args:
        QWidget
    """
    
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        
        #search bar initialisation
        
        self.layout:QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.lineEdit = QLineEdit(self)
        
        self.nameLabel = QLabel(self)
        
        self.filtered = []
        
        self.lineEdit.textChanged.connect(self.filterSearch)
        
        self.initUI()
        
    def initUI(self) :
        """ Initialisation de l'interface utilisateur de la barre de recherche
        """
        
        #initialisation des Widgets
        
        self.layout.addWidget(self.nameLabel)
        
        self.layout.addWidget(self.lineEdit)
        
        self.layout.addStretch()
        
        self.nameLabel.setText('Type your search :')
        
    def filterSearch(self) :
        """ Réalise la recherche en fonction du texte entrée
        """

        text = self.lineEdit.text()
        text = text.lower() 
        
        self.filtered = []
        
        if text in TYPES :
            text = TYPES[text]
            
        if text in TYPES.values() :
            
            with open('pokedex.json') as f:
                contenu = json.load(f)
                
            for pokemon in contenu :
                p_type = [t.lower() for t in pokemon['type']]
                if text in p_type :
                    self.filtered.append(pokemon['id'])
                    
            print(self.filtered)
        else : 
            with open('pokedex.json') as f:
                contenu = json.load(f)
                
            for pokemon in contenu :
                # p_name_en = [t.lower() for t in pokemon['name']['english']]
                p_name_fr = [pokemon['name']['french'].lower()]
                """  for poke_en in p_name_en :
                    if poke_en.startswith(text) :
                        self.filtered.append(pokemon['id']) """
                for poke_fr in p_name_fr: 
                    
                    if poke_fr.startswith(text) :
                        self.filtered.append(pokemon['id'])
                        
                        
                
                        