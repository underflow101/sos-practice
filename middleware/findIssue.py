'''
middleware/findIssue.py

- explains people how to find new issue
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import webbrowser

from configs.configuration import *

class FindIssueApp(QDialog):
    def __init__(self, parent, currentOS):
        super(FindIssueApp, self).__init__(parent)
        self.os = currentOS
        self.initUI()
    
    def initUI(self):
        self.config = mainUI()
        self.strings = strings()
        self.txtLen = len(self.strings.goodFirstIssue)
        
        height = self.config.btnHeight
        width = self.config.btnWidth
        sHeight = self.config.smlBtnHeight
        sWidth = self.config.smlBtnWidth
        
        self.step = 0
        
        # Txt 0: Introducing how to find good issues
        self.txt = QTextBrowser()
        self.txt.setAcceptRichText(True)
        self.txt.setOpenExternalLinks(True)
        self.issueFinderHandler()
        
        # Btn 0: Prev
        self.btnPrev = QPushButton(self)
        self.btnPrev.setText('<< Prev')
        self.btnPrev.setToolTip('Go to previous page')
        self.btnPrev.setMaximumHeight(sHeight)
        self.btnPrev.setMaximumWidth(sWidth)
        self.btnPrev.setEnabled(False)
        self.btnPrev.clicked.connect(self.prevHandler)
        
        # Btn 1: Next
        self.btnNext = QPushButton(self)
        self.btnNext.setText('Next >>')
        self.btnNext.setToolTip('Go to next page')
        self.btnNext.setMaximumHeight(sHeight)
        self.btnNext.setMaximumWidth(sWidth)
        self.btnNext.setEnabled(True)
        self.btnNext.clicked.connect(self.nextHandler)
        
        # Btn 4: Exit
        self.btnExit = QPushButton(self)
        self.btnExit.setText('Exit')
        self.btnExit.setToolTip('Close this Window')
        self.btnExit.setMaximumHeight(sHeight)
        self.btnExit.setMaximumWidth(sWidth)
        self.btnExit.clicked.connect(self.ExitHandler)
        
        # Grid Layout: list out buttons
        grid = QGridLayout()
        grid.addWidget(QLabel(self.tr("OS:")), 0, 0)
        grid.addWidget(QLabel(self.os), 0, 1)
        
        grid.addWidget(QLabel(self.tr("How to Find Good First Issue:")), 1, 0)
        grid.addWidget(self.txt, 2, 0)
        
        grid.addWidget(self.btnExit, 3, 0)
        grid.addWidget(self.btnPrev, 3, 1)
        grid.addWidget(self.btnNext, 3, 2)
        
        self.setWindowTitle('How to Find a Good First Issue?')
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(500, 500)
        self.setLayout(grid)
        self.show()
    
    def issueFinderHandler(self):
        self.txt.clear()
        self.txt.append(self.strings.goodFirstIssue[self.step])
                
    def prevHandler(self):
        self.step -= 1
        if self.step == 0:
            self.btnPrev.setEnabled(False)
        if self.step == (self.txtLen-2):
            self.btnNext.setEnabled(True)
        self.issueFinderHandler()
    
    def nextHandler(self):
        self.step += 1
        if self.step == 1:
            self.btnPrev.setEnabled(True)
        if self.step == (self.txtLen-1):
            self.btnNext.setEnabled(False)
        self.issueFinderHandler()
    
    def ExitHandler(self):
        self.close()
        return