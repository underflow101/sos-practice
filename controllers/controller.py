import sys, os
from random import randint
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QWidget, QPushButton, QDesktopWidget, QLabel
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QComboBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import webbrowser

class sosTutorialApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        '''
        * variables
        
        @param
        - height: Button layouts
            - param name        :   height
            - param range       :   0 ~ 216
            - param description :   changes height of buttons
            
        - width: Button layouts
            - param name        :   width
            - param range       :   0 ~ 720
            - param description :   changes width of buttons
        '''
        height = 50
        width = 1080
        
        '''
        * Combo Box
        
        @param
        - Combo Box 1: Category
            - param name        :   category
            - param range       :   selective for category (set, ala carte, soup, rice, etc.)
            - param description :   user can either select category or randomly select with this combo box
        '''
        self.category = QComboBox()
        self.res = None
        
        '''
        * Serial Input Buttons
        * Modify these buttons in order to modify/change name of the buttons or number of the buttons
        
        @param
        - Button 1: Randomize Category button
            - param name        :   randCat
            - param range       :   X
            - param description :   changes category randomly
            - param shortcut    :   Alt + 1
        
        - Button 2: Randomize button
            - param name        :   randAll
            - param range       :   X
            - param description :   changes frequency of PWM (Hz)
                                    avoid 10kHz to prevent tinnitus
            - param shortcut    :   Alt + 2
        '''
        
        # Button 1: Random Category button
        self.randCat = QPushButton(self)
        self.randCat.setText('&1. 분류 랜덤화')
        self.randCat.setToolTip("분류를 임의로 고릅니다.")
        self.randCat.setMaximumHeight(height)
        self.randCat.setMaximumWidth(width)
        self.randCat.clicked.connect(self.randCatHandler)
        
        # Button 2: Randomize button
        self.randAll = QPushButton(self)
        self.randAll.setText('&2. 랜덤!')
        self.randAll.setToolTip("랜덤 주사위를 던집니다.")
        self.randAll.setMaximumHeight(height)
        self.randAll.setMaximumWidth(width)
        self.randAll.clicked.connect(self.randAllHandler)
        
        # QUIT button
        quitBtn = QPushButton(self)
        quitBtn.setText('3. &Exit the Program')
        quitBtn.setToolTip("Exit the program")
        quitBtn.setMaximumHeight(height)
        quitBtn.setMaximumWidth(width)
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        
        # Grid Layout: list out buttons
        grid = QGridLayout()
        grid.addWidget(QLabel(self.tr("분류 선택")), 0, 0)
        grid.addWidget(self.category, 0, 1)
        grid.addWidget(QLabel(self.tr("분류를 임의로 고릅니다.")), 2, 0)
        grid.addWidget(self.randCat, 2, 1)
        grid.addWidget(QLabel(self.tr("메뉴를 임의로 고릅니다.")), 3, 0)
        grid.addWidget(self.randAll, 3, 1)
        grid.addWidget(QLabel(self.tr("프로그램을 종료합니다.")), 4, 0)
        grid.addWidget(quitBtn, 4, 1)
        
        # Put category inside
        self.category.insertItems(0, self.getCategory())
        
        self.setWindowTitle("Lunch Selector ver.Bon Dosirak")
        self.setWindowIcon(QIcon('dice.png'))
        self.resize(300, 300)
        self.center()
        self.setLayout(grid)
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    #######################################################################################
    # Event Handlers
    #
    # Each event handlers match to each buttons above.
    #######################################################################################
    def getCategory(self):
        self.categories = [
            '랜덤',
            '세트',
            '단품',
            '반찬',
            '국',
            '밥',
            '기타',
        ]
        return self.categories
    
    def randCatHandler(self):
        reply = QMessageBox.question(self, 'Message', "분류를 임의로 고르시겠습니까?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            idx = randint(1, 6)
            self.currentCateg = self.categories[idx]
            self.category.setCurrentText(self.currentCateg)
            return
        else:
            return
    
    def randAllHandler(self):
        # if not Full Random
        if self.category.currentText() != self.categories[0]:
            # 1st category
            if self.category.currentText() == self.categories[1]:
                self.res = self.returnSet()
                reply = QMessageBox.question(self, 'Message', self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
            # 2nd category
            elif self.category.currentText() == self.categories[2]:
                self.res = self.returnAlacarte()
                reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
            # 3rd category
            elif self.category.currentText() == self.categories[3]:
                self.res = self.returnSide()
                reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
            # 4th category
            elif self.category.currentText() == self.categories[4]:
                self.res = self.returnSoup()
                reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
            # 5th category
            elif self.category.currentText() == self.categories[5]:
                self.res = self.returnRice()
                reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
            # 6th category
            elif self.category.currentText() == self.categories[6]:
                self.res = self.returnEtc()
                reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    return
                else:
                    return
        else:
            self.candidate = list()
            self.candidate.append(self.returnSet())
            self.candidate.append(self.returnAlacarte())
            self.candidate.append(self.returnSide())
            self.res = self.lastRand(self.candidate)
            reply = QMessageBox.question(self, 'Message', "오늘의 메뉴:\n" + self.res,
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                return
            else:
                return
        return
    
    ##########################################################################################
    # Menu
    ##########################################################################################
    def returnSet(self):
        menu = [
            '봄달래쭈꾸미우삼겹도시락세트(10900)',
            '봄냉이우삼겹된장찌개도시락세트(9200)',
            '대구식매운찜갈비도시락세트(9900)',
            '대구식연탄불고기도시락세트(7900)',
            '고추장닭불고기쌈밥도시락세트(10200)',
            '고추장닭불고기도시락세트(쌈제외)(8900)',
            '여수꼬막불고기도시락세트(8900)',
            '속초식오징어바싹불고기도시락세트(8900)',
            '버섯불고기도시락세트(쌈제외)(8400)',
            '우리돼지등심돈까스도시락세트(7900)',
            '부추제육볶음도시락세트(쌈제외)(7900)',
            '돼지고기묵은지찌개도시락세트(7700)',
            '광양식바싹불고기도시락세트(7400)',
            '담양식떡갈비도시락세트(6900)',
            '속초식오징어볶음도시락세트(9900)',
            '춘천식닭구이도시락세트(8400)',
            '의정부식부대두루치기도시락세트(7400)',
            '버섯불고기쌈밥도시락세트(9700)',
            '부추제육볶음도시락세트(쌈제외)(9200)',
            '우렁강된장쌈밥도시락세트(9200)',
            '얼큰소고기가마솥국밥도시락세트(7900)',
            '제주모자반쇠고기미역국도시락세트(7700)'
        ]
        idx = randint(0, 21)
        return menu[idx]
    
    def returnAlacarte(self):
        menu = [
            '봄달래주꾸미우삼겹도시락(9200)',
            '봄냉이우삽겹된장찌개도시락(5300)',
            '봄냉이된장덮밥(5400)',
            '대구식매운찜갈비도시락(8200)',
            '대구식연탄불고기도시락(6200)',
            '진품닭불고기도시락(14000)',
            '고추장닭불고기쌈밥도시락(8500)',
            '고추장닭불고기도시락(쌈제외)(7200)',
            '새우아보카도샐러드(6500)',
            '일품불고기도시락(11000)',
            '여수꼬막불고기도시락(7200)',
            '속초오징어바싹불고기도시락(7200)',
            '버섯불고기도시락(쌈제외)(6700)',
            '우리돼지등심돈까스도시락(6200)',
            '부추제육볶음도시락(쌈제외)(6200)',
            '돼지고기묵은지찌개도시락(5100)',
            '광양식바싹불고기도시락(5700)',
            '담양식떡갈비도시락(5200)',
            '델리팸김치볶음밥(곱빼기)(5700)',
            '델리팸김치볶음밥(5200)',
            '궁중한정식도시락(23000)',
            '명품갈비구이도시락(18000)',
            '명이오리구이쌈도시락(15000)',
            '속초식오징어볶음도시락(8200)',
            '춘천식닭구이도시락(6700)',
            '의정부식부대두루치기도시락(5700)',
            '버섯불고기쌈밥도시락(8000)',
            '부추제육볶음도시락(7500)',
            '우렁강된장쌈밥도시락(7500)',
            '갈비생일상도시락(20000)',
            '소불고기생일상도시락(6500)',
            '허브닭가슴살샐러드(6500)',
            '고구마닭가슴살샐러드(5900)',
            '고구마견과류샐러드(4900)',
            '얼큰소고기가마솥국밥도시락(5300)',
            '제주모자반쇠고기미역국도시락(5100)',
            '치킨마요(곱빼기)(5400)',
            '치킨마요(4900)'
        ]
        idx = randint(0, 37)
        return menu[idx]
    
    def returnSide(self):
        menu = [
            '핫윙(7900)',
            '닭강정(7200)',
            '찹쌀탕수육(6500)',
            '버섯불고기반찬(5900)',
            '부추제육볶음반찬(5600)',
            '속초오징어바싹불고기반찬(5600)',
            '궁중잡채반찬(5400)',
            '우리돼지등신돈까스반찬(5400)',
            '광양식바싹불고기반찬(4900)'
        ]
        idx = randint(0, 8)
        return menu[idx]
    
    def returnSoup(self):
        menu = [
            '봄냉이우삽겹된장찌개도시락(4100)',
            '얼큰소고기가마솥국밥(4100)',
            '제주모자반쇠고기미역(3900)',
            '돼지고기묵은찌개(3900)',
            '미니국(2000)'
        ]
        idx = randint(0, 4)
        return menu[idx]
    
    def returnRice(self):
        menu = [
            '곤드레밥(3500)',
            '흑미밥(2000)',
        ]
        idx = randint(0, 1)
        return menu[idx]
    
    def returnEtc(self):
        menu = [
            '쌈채소(2000)',
            '핫윙두조각(1800)',
            '아이스홍시(1500)',
            '단호박식혜(1000)',
            '콜라(1500)',
            '사이다(1500)',
            '계란후라이추가(1000)',
            '델리햄한조각(700)',
            '컵국(미소된장)(600)',
            '컵국(미역국)(600)',
            '참고소한김(200)'
        ]
        idx = randint(0, 10)
        return menu[idx]
    
    def lastRand(self, menus):
        tmp = len(menus) - 1
        idx = randint(0, tmp)
        return menus[idx]