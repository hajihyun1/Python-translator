import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import googletrans
from gtts import gTTS
from playsound import playsound



form_class = uic.loadUiType("ui.ui")[0]


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.btnclicked)
        self.play.clicked.connect(self.playclicked)

    def btnclicked(self):
        #print(self.text.toPlainText())
        translator = googletrans.Translator()
        str1 = self.text.toPlainText()
        #print(self.l_code.toPlainText())
        result1 = translator.translate(str1, dest=self.l_code.toPlainText())
        #print(result1.text)
        self.print.setPlainText(result1.text)
        #소리재생
        tts = gTTS(text=self.print.toPlainText(),lang=self.l_code.toPlainText())
        tts.save("hello.mp3")
        print("음성 파일 hello.mp3가 생성되었습니다.")


    def playclicked(self):
        playsound("hello.mp3")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()