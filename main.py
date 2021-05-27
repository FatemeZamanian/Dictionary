# This Python file uses the following encoding: utf-8
import sys
import os
from functools import partial

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class dictionary(QWidget):
    def __init__(self):
        super(dictionary, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.words = []
        self.user=''
        self.ans=''
        fle = open('dictionary.txt', encoding="utf8")
        bf = fle.read()
        wrd = bf.split('\n')
        i = 0
        self.ui.show()


        self.ui.txt_p.textChanged.connect(self.translate)
        self.ui.rbtn_pTe.clicked.connect(self.setMode)
        self.ui.rbtn_eTp.clicked.connect(self.setMode)

        while i < len(wrd) - 1:

            dict_e = {'English': wrd[i], 'Persian': wrd[i + 1]}
            self.words.append(dict_e)
            i += 2

    def setMode(self):

        if self.ui.rbtn_pTe.isChecked():
            self.ui.txt_e.setReadOnly(True)
            self.ui.txt_p.setReadOnly(False)
            self.ui.txt_p.textChanged.connect(self.translate)
            try:
                self.ui.txt_e.textChanged.disconnect()
            except:
                pass

        elif self.ui.rbtn_eTp.isChecked():
            self.ui.txt_p.setReadOnly(True)
            self.ui.txt_e.setReadOnly(False)
            self.ui.txt_e.textChanged.connect(self.translate)
            try:
                self.ui.txt_p.textChanged.disconnect()
            except:
                pass


    def translate(self):

        if self.ui.rbtn_pTe.isChecked():
            user_text = self.ui.txt_p.toPlainText()
            user_sentences = user_text.split('.')
            temp = ''
            for user_sentence in user_sentences:
                user_words = user_sentence.split(' ')
                for user_word in user_words:
                    for i in range(len(self.words)):
                        if self.words[i]['Persian'] == user_word:
                            temp += self.words[i]['English'] + ' '
                            break
                    else:
                        temp += user_word + ' '
            self.ui.txt_e.setText(temp)

        elif self.ui.rbtn_eTp.isChecked():
            user_text = self.ui.txt_e.toPlainText()
            user_sentences = user_text.split('.')
            temp = ''
            for user_sentence in user_sentences:
                user_words = user_sentence.split(' ')
                for user_word in user_words:
                    for i in range(len(self.words)):
                        if self.words[i]['English'] == user_word:
                            temp += self.words[i]['Persian'] + ' '
                            break
                    else:
                        temp += user_word + ' '

            self.ui.txt_p.setText(temp)

if __name__ == "__main__":
    app = QApplication([])
    widget = dictionary()
    sys.exit(app.exec())
