from PySide6.QtWidgets import  *
from PySide6.QtCore import *
from assets.constante import *
import sys
import json
import hashlib

with open(BDD) as f:
    contenu = json.load(f)
    
def restart():
    QCoreApplication.quit()
    status = QProcess.startDetached(sys.executable, sys.argv)
    print(status)
    
class User():
    """ Va permettre d'obtenir les informations de l'utilisateur"""
    
    def __init__(self):
        self.username = contenu["lastConnected"] if contenu["lastConnected"] != "" else ""
        self.nb_pokemon = len(contenu["users"][self.username]["pokedex"]) if self.username != "" else 0
        self.userType = contenu["users"][self.username]["isAdmin"] if self.username != "" else False
    
class Connexion(QWidget) :
    """ Va permettre de se connecter"""
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        
        self.formLayout = QFormLayout()
        self.setLayout(self.formLayout)
        
        username_label = QLabel("Nom d'utilisateur : ")
        self.userLine = QLineEdit(self)
        
        password_label = QLabel("Mot de passe : ")
        self.passwordLine = QLineEdit(self)
        self.passwordLine.setEchoMode(QLineEdit.Password)
        
        self.loginButton = QPushButton("Login")
        self.loginButton.clicked.connect(self.login)
        
        self.formLayout.addRow(username_label, self.userLine)
        self.formLayout.addRow(password_label, self.passwordLine)
        self.formLayout.addRow(self.loginButton)
        self.formLayout
        
    def login(self): 
        
        username = self.userLine.text()
        
        if self.verifLogin() :
            contenu["lastConnected"] = username
                
            with open(BDD, "w") as f:
                json.dump(contenu, f , indent=6)
                
        else :
                print("Erreur de co")
        
        self.userLine.setText("")
        self.passwordLine.setText("")
    
        
    
    def verifLogin(self) :
        username = self.userLine.text()
        password = self.passwordLine.text()
        
        sha512 = hashlib.sha512()
        sha512.update(bytes(password, 'utf-8'))
        password = sha512.hexdigest()
        answer = False
        
        if username in contenu["users"] :
            if password == contenu["users"][username]['password'] :
                answer = True
        return answer

class Logged(QWidget):
    """ Va permettre d'afficher la page de l'utilisateur connecté"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = User()
        self.init_logged()

    def init_logged(self):
        """Initialise l'interface utilisateur"""
        self.formLayout = QVBoxLayout()
        self.setLayout(self.formLayout)

        self.userLabel = QLabel()
        self.nbPokemonLabel = QLabel()
        self.userTypeLabel = QLabel()
        self.disconnectButton = QPushButton()
        self.disconnectButton.clicked.connect(self.disconnect)

        self.formLayout.addWidget(self.userLabel)
        self.formLayout.addWidget(self.nbPokemonLabel)
        self.formLayout.addWidget(self.userTypeLabel)
        self.formLayout.addStretch()
        self.formLayout.addWidget(self.disconnectButton)

        self.update_logged()

    def update_logged(self):
        """Met à jour l'interface utilisateur"""
        self.user = User()
        self.userLabel.setText(f"Utilisateur : {self.user.username}")
        self.nbPokemonLabel.setText(f"Nombre de pokémon : {self.user.nb_pokemon}")
        self.userTypeLabel.setText(f"Type d'utilisateur : {'Administrateur' if self.user.userType else 'Membre'}")
        self.disconnectButton.setText('Déconnexion')

    def disconnect(self):
        """Déconnecte l'utilisateur et met à jour l'interface"""
        contenu['lastConnected'] = ""
        with open(BDD, "w") as f:
            json.dump(contenu, f, indent=6)