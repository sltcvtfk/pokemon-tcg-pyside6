from PySide6.QtWidgets import  QLabel, QLineEdit, QFormLayout, QPushButton, QWidget

import json

class Connexion(QWidget) :
    
    def __init__(self, parent=None) :
        super().__init__(parent)
        
        self.formLayout:QFormLayout = QFormLayout()
        self.setLayout(self.formLayout)
        
        username_label = QLabel("Username : ")
        self.userLine = QLineEdit(self)
        
        password_label = QLabel("Password : ")
        self.passwordLine = QLineEdit(self)
        self.passwordLine.setEchoMode(QLineEdit.Password)
        
        self.loginButton = QPushButton("Login")
        
        self.formLayout.addRow(username_label, self.userLine)
        self.formLayout.addRow(password_label, self.passwordLine)
        self.formLayout.addRow(self.loginButton)
        
    def login(self): 
        
        with open('user.json') as f:
                contenu = json.load(f)
    