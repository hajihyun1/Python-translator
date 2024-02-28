import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import googletrans



form_class = uic.loadUiType("ui.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.btnclicked)

    def btnclicked(self):
        #print(self.text.toPlainText())
        translator = googletrans.Translator()
        str1 = self.text.toPlainText()
        result1 = translator.translate(str1, dest='en')
        #print(result1.text)
        self.print.setPlainText(result1.text)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()