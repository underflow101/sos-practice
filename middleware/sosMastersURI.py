'''
middleware/sosMastersURI.py

- First button activity
- Send user to SOS Masters / Mine / Companions' homepage
'''

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import webbrowser

from configs.configuration import mainUI

class SosMasterApp(QDialog):
    def __init__(self, parent):
        super(SosMasterApp, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.config = mainUI()
        
        height = self.config.btnHeight
        width = self.config.btnWidth
        
        # Btn 0: SOS Masters github
        self.btnSosMastersGithub = QPushButton(self)
        self.btnSosMastersGithub.setText('SOS Masters Github')
        self.btnSosMastersGithub.setToolTip('Go to SOS Masters Github')
        self.btnSosMastersGithub.setMaximumHeight(height)
        self.btnSosMastersGithub.setMaximumWidth(width)
        self.btnSosMastersGithub.clicked.connect(self.SosMastersGithubHandler)
        
        # Btn 1: SOS Masters
        self.btnSosMasters = QPushButton(self)
        self.btnSosMasters.setText('SOS Masters')
        self.btnSosMasters.setToolTip('Go to SOS Masters Homepage')
        self.btnSosMasters.setMaximumHeight(height)
        self.btnSosMasters.setMaximumWidth(width)
        self.btnSosMasters.clicked.connect(self.SosMastersHandler)
        
        # Btn 2: SOS Mine
        self.btnSosMine = QPushButton(self)
        self.btnSosMine.setText('SOS Mine')
        self.btnSosMine.setToolTip('Go to SOS Mine Homepage')
        self.btnSosMine.setMaximumHeight(height)
        self.btnSosMine.setMaximumWidth(width)
        self.btnSosMine.clicked.connect(self.SosMineHandler)
        
        # Btn 3: SOS Companions
        self.btnSosCompanions = QPushButton(self)
        self.btnSosCompanions.setText('SOS Companions')
        self.btnSosCompanions.setToolTip('Go to SOS Companions Homepage')
        self.btnSosCompanions.setMaximumHeight(height)
        self.btnSosCompanions.setMaximumWidth(width)
        self.btnSosCompanions.clicked.connect(self.SosCompanionsHandler)
        
        # Btn 4: Exit
        self.btnExit = QPushButton(self)
        self.btnExit.setText('Exit')
        self.btnExit.setToolTip('Close this Window')
        self.btnExit.setMaximumHeight(height)
        self.btnExit.setMaximumWidth(width)
        self.btnExit.clicked.connect(self.ExitHandler)
        
        # Grid Layout: list out buttons
        grid = QGridLayout()
        grid.addWidget(QLabel(self.tr("SOS Masters Github")), 2, 0)
        grid.addWidget(self.btnSosMastersGithub, 2, 1)
        grid.addWidget(QLabel(self.tr("SOS Masters")), 3, 0)
        grid.addWidget(self.btnSosMasters, 3, 1)
        grid.addWidget(QLabel(self.tr("SOS Mine")), 4, 0)
        grid.addWidget(self.btnSosMine, 4, 1)
        grid.addWidget(QLabel(self.tr("SOS Companions")), 5, 0)
        grid.addWidget(self.btnSosCompanions, 5, 1)
        grid.addWidget(QLabel(self.tr("Exit")), 6, 0)
        grid.addWidget(self.btnExit, 6, 1)
        
        self.setWindowTitle('Link')
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(300, 500)
        self.setLayout(grid)
        self.show()
    
    def SosMastersGithubHandler(self):
        reply = QMessageBox.question(self, 'Message', "Go to Github?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            webbrowser.open('https://github.com/sos-masters/sos-masters')
            return
        else:
            return
    
    def SosMastersHandler(self):
        reply = QMessageBox.question(self, 'Message', "Go to Hompage?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            webbrowser.open('https://opensource.samsung.com/community/master/masterList')
            return
        else:
            return
        
    def SosMineHandler(self):
        reply = QMessageBox.question(self, 'Message', "Go to Hompage?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            webbrowser.open('https://opensource.samsung.com/community/mine/mineList')
            return
        else:
            return
    
    def SosCompanionsHandler(self):
        reply = QMessageBox.question(self, 'Message', "Go to Hompage?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            webbrowser.open('https://opensource.samsung.com/community/companions/companionsList')
            return
        else:
            return
    
    def ExitHandler(self):
        self.close()

        return