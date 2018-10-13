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


    def magic(self):
        self.text.setText(random.choice(self.hello))

    def paste(self):
        clipboard = QApplication.clipboard()
        clipboard.setText("password\n")
        mimeData = clipboard.mimeData()
    
        if mimeData.hasImage():
            self.setPixmap(mimeData.imageData())
        elif mimeData.hasHtml():
            self.text.setText(mimeData.html())
            self.text.setTextFormat(QtCore.Qt.RichText)
        elif mimeData.hasText():
            self.text.setText(mimeData.text())
            self.text.setTextFormat(QtCore.Qt.PlainText)
        else:
            self.text.setText(tr("Cannot display data"))

    def getText(self):
        (text, bool) = QtWidgets.QInputDialog.getText(None, "title", "label")
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec_())
