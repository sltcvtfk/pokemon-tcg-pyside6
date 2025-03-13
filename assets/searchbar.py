from PySide6.QtWidgets import  QWidget , QLabel, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from assets.constante import *
import json

# TYPES = { "eau" : "water",
#     "feu" : "fire",
#     "plante" : "grass",
#     "combat" : "fighting",
#     "normal" : "normal",
#     "glace" : "ice",
#     "insecte" : "bug",
#     "poison" : "poison",
#     "dragon" : "dragon",
#     "acier" : "steel",
#     "psy" : "psychic",
#     "sol" : "ground",
#     "ténèbres" : "dark",
#     "roche" : "rock",
#     "spectre" : "ghost",
#     "fée" : "fairy",
#     "vol" : "flying",
#     "électrik" : "electric"
# }
with open(POKEDEX, encoding="utf-8") as f:
    contenu = json.load(f)  
    
class Searchbar(QWidget) :
    """ Barre de recherche
    Args:
        QWidget
    """
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        
        # search bar initialisation
        
        self.layout:QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Search")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        
        
        
        
        self.lineEdit.setStyleSheet("border: 1px solid #bc545c; border-radius: 3px; text-align: center;")
        
        self.nameLabel = QLabel(self)
        
        self.filtered = []
        
        self.lineEdit.textChanged.connect(self.filterSearch)

        self.initUI()
        
        self.setGeometry(50, 600, 300, 100)
        
    def initUI(self) :
        """ Initialisation de l'interface utilisateur de la barre de recherche
        """
        
        # initialisation des Widgets
        
        self.layout.addWidget(self.nameLabel)
        
        self.layout.addWidget(self.lineEdit)
        
        self.layout.addStretch()
        
        #self.nameLabel.setText('Type your search :')
        
        # Set background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        #self.setContentsMargins(50, 0, 0, 30)
        #self.setFixedSize(300, 175) 
        
    def filterSearch(self) :
        """ Réalise la recherche en fonction du texte entrée
        """
        text = self.lineEdit.text()
        text = text.lower() 
       

        print(text)
        #self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        self.filtered = []
        
        if text in FRENCH_TYPE_TO_ENGLISH_DICT:
            text = FRENCH_TYPE_TO_ENGLISH_DICT[text]
            
            
        for pokemon in contenu :          
            if text in FRENCH_TYPE_TO_ENGLISH_DICT.values() :
                
                p_type = [t.lower() for t in pokemon['type']]
                if text in p_type :
                    self.filtered.append(pokemon['id'])
                #print(self.filtered)
            else : 
                p_name_fr = [pokemon['name']['french'].lower()]
                """  for poke_en in p_name_en :
                    if poke_en.startswith(text) :
                        self.filtered.append(pokemon['id']) """
                for poke_fr in p_name_fr: 
                    if poke_fr.startswith(text):
                        self.filtered.append(pokemon['id'])


    # def placeholderCenter(self):
    #     self.anim = QPropertyAnimation(self.lineEdit.text, b"pos")
    #     self.anim.setEasingCurve(QEasingCurve.InOutCubic)
    #     self.anim.setEndValue(QPoint(0, 500))
    #     self.anim.setDuration(4000)
    #     self.anim.start()
                    
                        
                            
                        
                
                        