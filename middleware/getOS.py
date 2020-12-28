'''
middleware/getOS.py

- Gets running Operating System of user
'''

import platform

def handle():
    OS = platform.system()
    osList = []
    tmpList = ['Windows', 'Darwin', 'Linux']
    
    osList.append(OS)
    for item in tmpList:
        if item not in osList:
            osList.append(item)
    
    return osList