from PySide6.QtWidgets import  QLabel, QLineEdit, QFormLayout, QPushButton, QWidget
from assets.constante import *
import json

with open(BDD) as f:
    contenu = json.load(f)
    
class Connexion(QWidget) :
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        
        self.formLayout = QFormLayout()
        self.setLayout(self.formLayout)
        
        username_label = QLabel("Username : ")
        self.userLine = QLineEdit(self)
        
        password_label = QLabel("Password : ")
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
            contenu["LastConnected"] = username
                
            with open(BDD, "w") as f:
                json.dump(contenu, f , indent=6)
                
        else :
                print("Erreur de co")
        
        self.userLine.setText("")
        self.passwordLine.setText("")
    
        
    
    def verifLogin(self) :
        username = self.userLine.text()
        password = self.passwordLine.text()
        answer = False
        
        if username in contenu["Users"] :
            if password == contenu["Users"][username]['password'] :
                answer = True
        return answer

class Logout(QWidget) :
    
    
    def __init__(self, parent=None) :
        super().__init__(parent)
    
        with open(BDD) as f:
            self.contenu = json.load(f)
    
        self.formLayout = QFormLayout()
        self.setLayout(self.formLayout)
    
        self.disconnectButton = QPushButton('Disconnect')
        self.disconnectButton.clicked.connect(self.disconnect)
        
        self.formLayout.addRow(self.disconnectButton)
        self.formLayout
        
    def disconnect(self) :
        
        contenu['LastConnected'] = ""
        
        with open(BDD, "w") as f:
                json.dump(contenu, f , indent=6)