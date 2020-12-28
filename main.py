'''
@title: sos-practice
@version: devel-v0.1
    - prototype version
@Dev: underflow101
'''

import webbrowser
import sys, os
from PyQt5.QtWidgets import QApplication
from middleware.appMain import sosTutorialApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = sosTutorialApp()
    sys.exit(app.exec_())