'''
configs/configuration.py

- Saves configuration of the program
'''

class mainUI:
    btnHeight = 50
    btnWidth = 1080
    
    smlBtnHeight = 20
    smlBtnWidth = 1080
    
    mainUIHeight = 300
    mainUIWidth = 300
    
    def __init__(self):
        super().__init__()
        
class gitOps:
    gitCliWindows = """To install Git on Windows,<br>
    1. Go to <b><a href="https://git-scm.com/">git-scm</a></b><br>
    2. Download Git Bash and install it to your computer<br>
    3. Launch Git Bash and let's practice how to use Git CLI!"""
    
    gitCliMacOS = """To install Git on MacOS,<br>
    1. Go to <b><a href="https://brew.sh/index_ko">brew</a></b><br>
    2. Copy <b>$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</b><br>
    3. Paste it on your terminal, and press Enter<br>
    4. Type <b>$ brew install git</b> on your terminal<br>
    5. Now you are good to go!"""
    
    gitCliLinux = """To install Git on Linux,<br><br>
    1. Launch your terminal<br>
    2. Copy <b>$ sudo apt install git</b><br>
    3. Press Enter<br>
    4. You are good to go!"""
    
    gitCmdAdd = """You can add your source codes by following commands:<br><br>
    1. <b>$ git add .</b> or <b>$ git add ~/dir/to/your/src.py</b><br>
    2. <b>$ git commit -s</b><br>
        2-1. Put your commit title, and description<br>
        2-2. Try to follow basic Git Commit Rules; you can learn this in this program!<br>
    3. <b>$ git push</b><br>
    4. Put your Git ID and Password<br>
    5. Done!"""
    
    def __init__(self):
        super().__init__()
        
class strings:
    gitOp = gitOps()
    gitManual = [[gitOp.gitCliLinux,
                  gitOp.gitCliMacOS,
                  gitOp.gitCliWindows],
                  gitOp.gitCmdAdd,
                 'test2',
                 'test3']
    
    def __init__(self):
        super().__init__()