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

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.text.setFont(QtGui.QFont("Titillium", 30))
        self.button.setFont(QtGui.QFont("Titillium", 20))
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
        self.button.clicked.connect(self.getText)

        button = QtWidgets.QPushButton('PASSWORD', self) # Create the button
        button.setFont(QtGui.QFont("Titillium", 80))
        button.clicked.connect(self.paste) # Cause the window to quit when button is clicked
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
        button2.resize(200,200) # Resize the button to the suggested height
        button2.move(0, 0) # Move where the button is located
        self.layout.addWidget(button2)


    def magic(self):
        self.text.setPlainText(random.choice(self.hello))

    def paste(self):
        clipboard = QApplication.clipboard()
        clipboard.setPlainText("123qwe!@#QWE\n")
        mimeData = clipboard.mimeData()
    
        if mimeData.hasImage():
            self.setPixmap(mimeData.imageData())
        elif mimeData.hasHtml():
            self.text.setPlainText(mimeData.html())
            self.text.setTextFormat(QtCore.Qt.RichText)
        elif mimeData.hasText():
            self.text.setPlainText(mimeData.text())
            self.text.setTextFormat(QtCore.Qt.PlainText)
        else:
            self.text.setPlainText(tr("Cannot display data"))

    def paste1(self):
        #clipboard = QApplication.clipboard()
        #clipboard.setPlainText("123qwe!@#QWE\n")
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
        else:
            print ('not match')

        self.text.setText(raw_text)
        
    def getText(self):
        (text, bool) = QtWidgets.QInputDialog.getText(None, "title", "label")
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
