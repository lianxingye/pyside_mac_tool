# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QSpinBox, QApplication

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",\
            "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Procedure")
        self.button.setStyleSheet("background-color:rgb(195, 155, 211)");

        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.text.setFont(QtGui.QFont("Titillium", 30))
        self.button.setFont(QtGui.QFont("Titillium", 80))
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.textedit = QtWidgets.QPlainTextEdit()
        self.textedit.setReadOnly(False)
        self.textedit.setPlainText("hello edit")
        self.cursor = self.textedit.textCursor()
        self.cursor.insertText("[Cursor Input]")
        self.layout.addWidget(self.textedit)
        #self.button.clicked.connect(self.magic)
        self.button.clicked.connect(self.getTextPR)

        button = QtWidgets.QPushButton('LOGIN', self) # Create the button
        button.setFont(QtGui.QFont("Titillium", 80))
        button.clicked.connect(self.paste) # Cause the window to quit when button is clicked
        button.setStyleSheet("background-color:rgb(231, 76, 60)");
        button.resize(200,200) # Resize the button to the suggested height
        button.move(0, 0) # Move where the button is located

        button1 = QtWidgets.QPushButton('EXIT', self) # Create the button
        button1.clicked.connect(QApplication.instance().quit) # Cause the window to quit when button is clicked
        button1.resize(200,200) # Resize the button to the suggested height
        button1.move(200, 0) # Move where the button is located

        self.layout.addWidget(button)

        self.layout.addWidget(button1)

        button2 = QtWidgets.QPushButton('exclude #', self) # Create the button
        button2.setFont(QtGui.QFont("Titillium", 80))
        button2.clicked.connect(self.paste1) # Cause the window to quit when button is clicked
        button2.setStyleSheet("background-color:rgb(229, 152, 102)");
        button2.resize(200,200) # Resize the button to the suggested height
        button2.move(0, 0) # Move where the button is located
        self.layout.addWidget(button2)

        button2 = QtWidgets.QPushButton('work on ticket', self) # Create the button
        button2.setFont(QtGui.QFont("Titillium", 80))
        button2.clicked.connect(self.workon) # Cause the window to quit when button is clicked
        button2.setStyleSheet("background-color:rgb(93, 173, 226)");
        button2.resize(200,200) # Resize the button to the suggested height
        button2.move(0, 0) # Move where the button is located
        self.layout.addWidget(button2)

        self.addbutton("PR", self.PRCopy, "background-color:rgb(247, 220, 111)")

        self.addbutton("Proxy", self.getProxyExport, "background-color:rgb(82, 190, 128)")

        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(self.tr("Ctrl+W", "Exit")),
                     self)


    def addbutton(self, title, target_func, color_str):
        button2 = QtWidgets.QPushButton(title, self) # Create the button
        button2.setFont(QtGui.QFont("Titillium", 80))
        button2.clicked.connect(target_func) # Cause the window to quit when button is clicked
        button2.setStyleSheet(color_str);
        button2.resize(200,200) # Resize the button to the suggested height
        button2.move(0, 0) # Move where the button is located
        self.layout.addWidget(button2)

    def PRCopy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("Reference\nTRVINFRA-xxxxx\nOPEKAI-xxxxx\n\nOperation Target\nmon-traltmgr1\n\nOutline\nxxxxx\n\nJenkins\nhttp://dev-qtrsys101z.dev.jp.local/jenkins/job/docker_TEST_ALL_ENV/xxxx/console\n")
        mimeData = clipboard.mimeData()
   
        import string 
        if mimeData.hasText():
            self.text.setText(''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))
            self.text.setTextFormat(QtCore.Qt.PlainText)
        else:
            self.text.setPlainText(tr("Cannot display data"))

    def workon(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        self.textedit.setPlainText(mimeData.text())
        if 'TRVINFRA' not in mimeData.text():
          #(text, bool) = QtWidgets.QInputDialog.getText(None, "No TRVINFRA", "No TRVINFRA")

          #er = QtWidgets.QErrorMessage(self)
          #er.showMessage("can not find ticket id")
          msgBox = QtWidgets.QMessageBox()
          msgBox.setText("can not find ticket id");
          #msgBox.exec_();

          #msgBox = QtWidgets.QMessageBox(self)
          #msgBox.setText("invalid ticket id in edit box")
          #msgBox.exec_()
          return
        import re

        text = mimeData.text()
        
        m = re.search('TRVINFRA-(\d+)', text)
        if m:
            found = m.group(1)
            self.text.setText(found)
            self.current_ticket_num=found

        self.textedit.setPlainText("TRVINFRA-"+found)
        clipboard = QApplication.clipboard()
        clipboard.setText("TRVINFRA-"+found)


        self.createbranch("TRVINFRA-"+found)

        import jenkins

        server = jenkins.Jenkins('http://dev-qtrsys101z.dev.jp.local/jenkins/', username='lianxing.a.ye', password='qwe123QWE')

        #server.build_job('docker_TEST_ALL_ENV', {'TARGET': 'mon-traltmgr1', 'branch_name': 'TRVINFRA-20545', 'recipe': 'trv_prometheus', 'spec_name': 'trv_prometheus', 'target_env': 'dev', 'custom_command': 'uname -a'})
        #self.openweb('http://dev-qtrsys101z.dev.jp.local/jenkins/job/docker_TEST_ALL_ENV/')

        #self.openweb("https://jira.rakuten-it.com/jira/browse/"+self.textedit.toPlainText())

    def magic(self):
        self.text.setPlainText(random.choice(self.hello))

    def paste(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("qwe123QWE\n")
        mimeData = clipboard.mimeData()
   
        import string 
        if mimeData.hasText():
            self.text.setText(''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))
            self.text.setTextFormat(QtCore.Qt.PlainText)
        else:
            self.text.setPlainText(tr("Cannot display data"))

    def paste1(self):
        #clipboard = QApplication.clipboard()
        #clipboard.setPlainText("xxxxxxxxxxxxxxx\n")
        #mimeData = clipboard.mimeData()

        #raw_text = mimeData.text()

    
        #if mimeData.hasImage():
        #    self.setPixmap(mimeData.imageData())
        #elif mimeData.hasHtml():
        #    self.textedit.setPlainText(mimeData.text())
        #elif mimeData.hasText():
        #    self.textedit.setPlainText(mimeData.text())
        #else:
        #    self.text.setPlainText(tr("Cannot display data"))
        self.cursor = self.textedit.textCursor()

        self.cursor.movePosition(QtGui.QTextCursor.Down)
        self.textedit.setTextCursor(self.cursor)
        self.cursor.select(QtGui.QTextCursor.LineUnderCursor)
        self.textedit.setTextCursor(self.cursor)

        self.textedit.copy()

        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        raw_text = mimeData.text()

        import re

        if re.match(r'^( )*#', raw_text):
            print ('match')
            print (raw_text.replace("#", "", 1))
            raw_text = raw_text.replace("#", "", 1)
        elif re.match(r'^( )*\$', raw_text):
            print ('match')
            print (raw_text.replace("$", "", 1))
            raw_text = raw_text.replace("$", "", 1)
        else:
            print ('not match')

        self.text.setText(raw_text)
        clipboard.setText(raw_text+"\n")
        
    def getTextPR(self):
        clipboard = QApplication.clipboard()

        pr_desc='[Request Ticket]\n \n[Opekai Ticket]\n \n- Log (depman)\n$ ~/.depman/platform/depman_login.sh\n1, 2, 3 ... or x >$ 5\n$ 7010-000XXXXX\n\n*Procedure\n(DEV)\n  $ ssh dev-atrsysansible101z.dev.jp.local\n(STG)\n  $ ssh stg-atrsysansible101z.stg.jp.local\n(PROD)\n  $ ssh atrsysansible101z.prod.jp.local\n\n** Operation for TRAVEL environment\n$ RECIPE=[RECIPE]\n$ TARGET=[TARGET]\n$ cd ~/lei-ansible\n$ git pull origin master\n$ ansible-playbook -i hosts.`hostname -f | cut -d"." -f2` -k -K travel/run_recipe.yml -e recipe=${RECIPE} --list-hosts -l ${TARGET}\n$ ansible-playbook -i hosts.`hostname -f | cut -d"." -f2` -k -K travel/run_recipe.yml -e recipe=${RECIPE} -l ${TARGET}'
        clipboard.setText(pr_desc)
        #(text, bool) = QtWidgets.QInputDialog.getText(None, "title", "label")
        #print(text)
        
    def getProxyExport(self):
        clipboard = QApplication.clipboard()

        desc="export http_proxy=http://pkg.proxy.prod.jp.local:10080\nexport https_proxy=http://pkg.proxy.prod.jp.local:10080\n"
        clipboard.setText(desc)

    def openweb(self,weburl):
        import webbrowser
        url = weburl
        webbrowser.open_new(url)

    def createbranch(self, branch_name):
        import os
        os.system('cd /Users/lianxing.a.ye/Projects/trv-chef;git checkout -b '+branch_name)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
