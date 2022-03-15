#author Tray Keller

# Todo Write a way to add ssh keys to the menu
# maybe a bash script that runs and collects the data using a combination of find
# maybe using python and using the variables taken from sys to get the exported variables to get the data using python


import sys

from PyQt5.QtWidgets import *


#Creates base application
app = QApplication([])
app.setStyle("Fusion")
#Creates window
window = QWidget()
#Sets the window dimensions and title
window.setWindowTitle('sshvault')
window.setGeometry(500, 500, 500, 500)
#Layout starts here
TextScreen = QLabel("SSHKeys goes here")
render = QGridLayout()
ssh_key_btn = QPushButton("Add key")
render.addWidget(TextScreen)
render.addWidget(ssh_key_btn,1,0)




window.setLayout(render)
window.show()
sys.exit(app.exec_())
