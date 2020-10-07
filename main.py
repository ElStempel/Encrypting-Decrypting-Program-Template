from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

textFilePath = ""
keyFilePath = ""
saveFilePath = ""


class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno,self).__init__(*args,*kwargs)
        self.setWindowTitle("Maszyna szyfrująca/deszyfrująca")

        #########NAPISY#########
        
        titleText = QLabel()
        titleText.setText("Podaj tekst i klucz lub wybierz plik")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Arial',30))
        
        self.subtitleText = QLabel()
        self.subtitleText.setText("")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Arial',20))
        
        self.opisText = QLabel()
        self.opisText.setText("Aleksander Stęplewski 140784 \n Bez znaków polskich ani cyfr \n Przyjmuje tylko pliki .txt")
        self.opisText.setAlignment(Qt.AlignCenter)
        self.opisText.setFont(QFont('Arial',15))
        
        self.dzialanieText = QLabel()
        self.dzialanieText.setText("Maszyna do szyfru PLACEHOLDER")
        self.dzialanieText.setAlignment(Qt.AlignCenter)
        self.dzialanieText.setFont(QFont('Arial',35))
        
        self.messageField = QLineEdit()
        self.messageField.setPlaceholderText("Ustaw tekst...")
        
        self.keyField = QLineEdit()
        self.keyField.setPlaceholderText("Ustaw klucz...")
        
        textFieldsLayout = QHBoxLayout()
        textFieldsLayout.addWidget(self.messageField)
        textFieldsLayout.addWidget(self.keyField)
        textFieldsLayoutW = QWidget()
        textFieldsLayoutW.setLayout(textFieldsLayout)
        
        ######PRZYCISKI#######
        
        encryptButton = QPushButton()
        encryptButton.setText("Szyfruj")
        encryptButton.clicked.connect(self.encryptClicked)
        
        decryptButton = QPushButton()
        decryptButton.setText("Deszyfruj")
        decryptButton.clicked.connect(self.decryptClicked)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(decryptButton)
        buttonsLayoutW = QWidget()
        buttonsLayoutW.setLayout(buttonsLayout)
        
        textSelectButton = QPushButton()
        textSelectButton.setText("Wybierz plik tekstu")
        textSelectButton.clicked.connect(self.textSelectClicked)
        
        keySelectButton = QPushButton()
        keySelectButton.setText("Wybierz plik klucza")
        keySelectButton.clicked.connect(self.keySelectClicked)
        
        saveButton = QPushButton()
        saveButton.setText("Zapisz tekst do pliku")
        saveButton.clicked.connect(self.saveClicked)

        selectLayout = QHBoxLayout()
        selectLayout.addWidget(textSelectButton)
        selectLayout.addWidget(keySelectButton)
        selectLayoutW = QWidget()
        selectLayoutW.setLayout(selectLayout)
        
        saveLayout = QHBoxLayout()
        saveLayout.addWidget(saveButton)
        saveLayoutW = QWidget()
        saveLayoutW = QWidget()
        saveLayoutW.setLayout(saveLayout)
        
        #######WIDGETY#########
        
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(self.opisText)
        mainMenu.addWidget(self.dzialanieText)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(textFieldsLayoutW)
        mainMenu.addWidget(buttonsLayoutW)
        mainMenu.addWidget(selectLayoutW)
        mainMenu.addWidget(saveLayoutW)
        

        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)
        
    ######FUNKCJE########
    
    def encrypt(self):
        print("encrypt")
        
    def decrypt(self):
        print("decrypt")
           
    def encryptClicked(self):
        self.subtitleText.setText("Szyfruje " + self.messageField.text() + " kluczem " + self.keyField.text())
        self.encrypt()
    
    def decryptClicked(self):
        self.subtitleText.setText("Deszyfruje " + self.keyField.text() + " kluczem " + self.messageField.text())
        self.decrypt()
        
    def textSelectClicked(self):
        textFilePath = filedialog.askopenfilename()
        self.subtitleText.setText("Biorę tekst z: " + textFilePath)
        f = open(textFilePath, "r")
        text = f.read()
        f.close()
        self.messageField.setText(text)
        
    def keySelectClicked(self):
        keyFilePath = filedialog.askopenfilename()
        self.subtitleText.setText("Biorę klucz z: " + keyFilePath)
        f = open(keyFilePath, "r")
        key = f.read()
        f.close()
        self.keyField.setText(key)
        
    def saveClicked(self):
        self.subtitleText.setText("Zapisuje")
        saveFilePath = filedialog.asksaveasfilename()
        f = open(saveFilePath, "w")
        f.write(self.messageField.text())
        f.close
        


########MAIN##########

app = QApplication(sys.argv)
window = Okno()
#window.setFixedSize(800,600)
window.setStyleSheet("background-color: rgb(236,236,236)")
window.show()
app.exec_()
