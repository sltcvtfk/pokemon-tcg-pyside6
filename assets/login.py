from PySide6.QtWidgets import  QLabel, QLineEdit, QFormLayout, QPushButton, QWidget
from assets.constante import *
import json

with open(BDD) as f:
    data = json.load(f)
    
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
        
        print("slt")
    