import sys, os
from random import randint
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QWidget, QPushButton, QDesktopWidget, QLabel
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import webbrowser

from configs.configuration import mainUI
from middleware import getOS
from middleware import sosMastersURI

class sosTutorialApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def initUI(self):
        self.config = mainUI()
        
        btnHeight = self.config.btnHeight
        btnWidth = self.config.btnWidth
        
        self.runningOS = QComboBox()
        self.runningOS.insertItems(0, getOS.handle())
        
        # Button 0: Link to URL
        self.btnLink = QPushButton(self)
        self.btnLink.setText('&Links')
        self.btnLink.setToolTip('Go to Links')
        self.btnLink.setMaximumHeight(btnHeight)
        self.btnLink.setMaximumWidth(btnWidth)
        self.btnLink.clicked.connect(self.linkHandler)
        
        # QUIT button
        btnQuit = QPushButton(self)
        btnQuit.setText('&Exit the Program')
        btnQuit.setToolTip("Exit the program")
        btnQuit.setMaximumHeight(btnHeight)
        btnQuit.setMaximumWidth(btnWidth)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        
        # Grid Layout: list out buttons
        grid = QGridLayout()
        grid.addWidget(QLabel(self.tr("OS:")), 0, 0)
        grid.addWidget(self.runningOS, 0, 1)
        grid.addWidget(QLabel(self.tr("Link to Pages")), 2, 0)
        grid.addWidget(self.btnLink, 2, 1)
        
        grid.addWidget(QLabel(self.tr("프로그램을 종료합니다.")), 4, 0)
        grid.addWidget(btnQuit, 4, 1)
        
        self.setWindowTitle("SOS Masters Practice")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(300, 300)
        self.center()
        self.setLayout(grid)
        self.show()
        
    def linkHandler(self):
        sosMastersURI.SosMasterApp(self)