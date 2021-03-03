import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

from configs.configuration import mainUI
from middleware import getOS, gitOperation, sosMastersURI, findIssue

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
        self.btnLink.setText('&SOS Program Links')
        self.btnLink.setToolTip('Go to Links')
        self.btnLink.setMaximumHeight(btnHeight)
        self.btnLink.setMaximumWidth(btnWidth)
        self.btnLink.clicked.connect(self.linkHandler)
        
        # Button 1: Basic git operations
        self.btnGitOp = QPushButton(self)
        self.btnGitOp.setText('&Basic Git')
        self.btnGitOp.setToolTip('Learn basic git operations')
        self.btnGitOp.setMaximumHeight(btnHeight)
        self.btnGitOp.setMaximumWidth(btnWidth)
        self.btnGitOp.clicked.connect(self.gitOpHandler)
        
        # Button 2: Good First Issue
        self.btnFirstIssue = QPushButton(self)
        self.btnFirstIssue.setText('&How to Find Issue')
        self.btnFirstIssue.setToolTip('Learn how to find first issue to solve and contribute')
        self.btnFirstIssue.setMaximumHeight(btnHeight)
        self.btnFirstIssue.setMaximumWidth(btnWidth)
        self.btnFirstIssue.clicked.connect(self.firstIssueHandler)
        
        # QUIT button
        btnQuit = QPushButton(self)
        btnQuit.setText('&Exit the Program')
        btnQuit.setToolTip("Exit the program")
        btnQuit.setMaximumHeight(btnHeight)
        btnQuit.setMaximumWidth(btnWidth)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)
        
        # Grid Layout: list out buttons
        grid = QGridLayout()
        grid.addWidget(QLabel(self.tr("Hi~ Welcome!! Let's Join SOS Practice Project")), 0, 0)
        grid.addWidget(QLabel(self.tr("Your Operating System is ")), 1, 0)
        grid.addWidget(self.runningOS, 1, 1)
        grid.addWidget(QLabel(self.tr("Reference")), 2, 0)
        grid.addWidget(self.btnLink, 2, 1)
        grid.addWidget(QLabel(self.tr("Basic Git Operations")), 3, 0)
        grid.addWidget(self.btnGitOp, 3, 1)
        grid.addWidget(QLabel(self.tr("How to Find Issue")), 4, 0)
        grid.addWidget(self.btnFirstIssue, 4, 1)
        grid.addWidget(QLabel(self.tr("프로그램을 종료합니다.")), 5, 0)
        grid.addWidget(btnQuit, 5, 1)
        
        self.setWindowTitle("SOS Practice for Master program & opensource contribution")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(self.config.mainUIWidth, self.config.mainUIHeight)
        self.center()
        self.setLayout(grid)
        self.show()
        
    def linkHandler(self):
        sosMastersURI.SosMasterApp(self)
        
    def gitOpHandler(self):
        gitOperation.GitTutorialApp(self, self.runningOS.currentText())
        
    def firstIssueHandler(self):
        findIssue.FindIssueApp(self, self.runningOS.currentText())