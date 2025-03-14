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
        self.loginButton.clicked.connect(restart)
        
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

        sha512 = hashlib.sha512() #Hachage du mot de passe pour le vérifier
        sha512.update(bytes(password, 'utf-8'))
        password = sha512.hexdigest()

        answer = False
        
        if username in contenu["users"] :
            if password == contenu["users"][username]['password'] :
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
        self.disconnectButton.clicked.connect(restart)
        
    def disconnect(self) :
        
        contenu['lastConnected'] = ""
        
        with open(BDD, "w") as f:
                json.dump(contenu, f , indent=6)