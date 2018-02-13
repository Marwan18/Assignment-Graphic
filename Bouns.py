from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from os import path
import os
import time
from PyQt5.uic import loadUiType
From_Desgin,_ = loadUiType(path.join(path.dirname(__file__),"marwan.ui"))

class Window(QMainWindow,From_Desgin):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    outer_counter = 0
    score = 0


    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        self.setFixedSize(474,336)
        self.setupUi(self)
        self.setWindowIcon(QIcon("photo.ico"))
        self.setWindowTitle("Memory Game")
        self.btn1.clicked.connect(self.Btn1)
        self.btn2.clicked.connect(self.Btn2)
        self.btn3.clicked.connect(self.Btn3)
        self.btn4.clicked.connect(self.Btn4)
        self.btn5.clicked.connect(self.Btn5)
        self.btn6.clicked.connect(self.Btn6)
        self.btn7.clicked.connect(self.Btn7)
        self.btn8.clicked.connect(self.Btn8)
        # self.btn9.clicked.connect(self.Btn9)





















        self.show()
    def different(self):
        self.btn7.setStyleSheet("background-color:black")
        self.btn1.setStyleSheet("background-color:black")
        self.btn5.setStyleSheet("background-color:black")
        self.btn4.setStyleSheet("background-color:black")
        self.btn3.setStyleSheet("background-color:black")
        self.btn6.setStyleSheet("background-color:black")
        self.btn8.setStyleSheet("background-color:black")
        self.btn2.setStyleSheet("background-color:black")

        self.btn7.setText("")
        self.btn8.setText("")
        self.btn1.setText("")
        self.btn3.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn2.setText("")
        self.btn4.setText("")


    def check(self):
        if self.score == 4 :
            self.box = QMessageBox.about(self,"Memory Game","Congratulation You Won ")

    def Btn1(self):

        self.btn1.setStyleSheet("background-color:red")
        self.btn1.setText("1")
        self.counter1 +=1

        if self.btn1.text() == "1" and self.btn2.text() == "2" :
            self.btn1.setStyleSheet("background-color:red")
            self.btn2.setStyleSheet("background-color:red")
            self.btn1.setText("")
            self.btn2.setText("")
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn1.setVisible(False)
            self.btn2.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")

            self.btn2.setText("")
            self.btn4.setText("")
            self.check()


        elif self.btn1.text() == "1" and self.btn3.text() == "3" :


            self.different()


        elif self.btn1.text() == "1" and self.btn4.text() == "4":

            self.different()

        elif self.btn1.text() == "1" and self.btn5.text() == "5":

            self.different()


        elif self.btn1.text() == "1" and self.btn6.text() == "6":
            self.different()


        elif self.btn1.text() == "1" and self.btn7.text() == "7":

            self.different()

        elif self.btn1.text() == "1" and self.btn8.text() == "8":

            self.different()


    def Btn2(self):
        self.btn2.setStyleSheet("background-color:red")
        self.counter1 += 1
        self.btn2.setText("2")

        if self.btn2.text() == "2" and self.btn1.text() == "1":
            self.btn1.setStyleSheet("background-color:red")
            self.btn2.setStyleSheet("background-color:red")
            self.btn1.setText("")
            self.btn2.setText("")
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn1.setVisible(False)
            self.btn2.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")

            self.btn2.setText("")
            self.btn4.setText("")
            self.check()



        elif self.btn2.text() == "2" and self.btn3.text() == "3" :

            self.different()

        elif self.btn2.text() == "2" and self.btn4.text() == "4":

            self.different()

        elif self.btn2.text() == "2" and self.btn5.text() == "5":

            self.different()


        elif self.btn2.text() == "2" and self.btn6.text() == "6":

            self.different()

        elif self.btn2.text() == "2" and self.btn7.text() == "7":

            self.different()

        elif self.btn2.text() == "2" and self.btn8.text() == "8":

            self.different()

    def Btn3(self):

        self.btn3.setStyleSheet("background-color:blue")
        self.counter2 +=1
        self.btn3.setText("3")
        if self.btn3.text() == "3" and self.btn1.text() == "1":


            self.different()

        elif self.btn3.text() == "3" and self.btn2.text() == "2":


            self.different()


        elif self.btn3.text() == "3" and self.btn4.text() == "4":
            self.btn3.setStyleSheet("background-color:blue")
            self.btn4.setStyleSheet("background-color:blue")
            self.btn1.setText("")
            self.btn3.setText("")

            self.btn2.setText("")
            self.btn4.setText("")
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn3.setVisible(False)
            self.btn4.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
        elif self.btn3.text() == "3" and self.btn5.text() == "5":
            self.different()
            self.check()



        elif self.btn3.text() == "3" and self.btn6.text() == "6":


            self.different()


        elif self.btn3.text() == "3" and self.btn7.text() == "7":


            self.different()

        elif self.btn3.text() == "3" and self.btn8.text() == "8":


            self.different()

    def Btn4(self):

        self.btn4.setStyleSheet("background-color:blue")
        self.counter2 +=1
        self.btn4.setText("4")

        if self.btn4.text() == "4" and self.btn1.text() == "1":
            self.different()


        elif self.btn4.text() == "4" and self.btn2.text() == "2":

            self.different()

        elif self.btn4.text() == "4" and self.btn3.text() == "3":
            self.btn3.setStyleSheet("background-color:blue")
            self.btn4.setStyleSheet("background-color:blue")
            self.btn2.setText("")
            self.btn4.setText("")
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn3.setVisible(False)
            self.btn4.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")

            self.btn2.setText("")
            self.btn4.setText("")
            self.check()

        elif self.btn4.text() == "4" and self.btn5.text() == "5":

            self.different()

        elif self.btn4.text() == "4" and self.btn6.text() == "6":
            self.different()

        elif self.btn4.text() == "4" and self.btn7.text() == "7":
            self.different()


        elif self.btn4.text() == "4" and self.btn8.text() == "8":
            self.different()


    def Btn5(self):

        self.btn5.setStyleSheet("background-color:green")
        self.btn5.setText("5")
        self.counter3 +=1

        if self.btn5.text() == "5" and self.btn6.text() == "6" :
            self.btn5.setStyleSheet("background-color:green")
            self.btn6.setStyleSheet("background-color:green")
            self.btn1.setStyleSheet("background-color:black")
            self.btn2.setStyleSheet("background-color:black")
            self.btn3.setStyleSheet("background-color:black")
            self.btn4.setStyleSheet("background-color:black")

            self.btn5.setText("")
            self.btn6.setText("")
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn5.setVisible(False)
            self.btn6.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn2.setText("")
            self.btn4.setText("")
            self.check()



        elif self.btn5.text() == "5" and self.btn1.text() == "1" :


            self.different()

        elif self.btn5.text() == "5" and self.btn4.text() == "4":

            self.different()

        elif self.btn5.text() == "5" and self.btn3.text() == "3":

            self.different()

        elif self.btn5.text() == "5" and self.btn2.text() == "2":

            self.different()

        elif self.btn5.text() == "5" and self.btn7.text() == "7":

            self.different()

        elif self.btn5.text() == "5" and self.btn8.text() == "8":

            self.different()

    def Btn6(self):

        self.btn6.setStyleSheet("background-color:green")
        self.btn6.setText("6")
        self.counter3 += 1

        if self.btn6.text() == "6" and self.btn5.text() == "5":
            self.btn5.setStyleSheet("background-color:green")
            self.btn6.setStyleSheet("background-color:green")
            self.btn1.setStyleSheet("background-color:black")
            self.btn2.setStyleSheet("background-color:black")
            self.btn3.setStyleSheet("background-color:black")
            self.btn4.setStyleSheet("background-color:black")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn5.setVisible(False)
            self.btn6.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn2.setText("")
            self.btn4.setText("")
            self.check()



        elif self.btn6.text() == "6" and self.btn3.text() == "3":

            self.different()

        elif self.btn6.text() == "6" and self.btn4.text() == "4":

            self.different()


        elif self.btn6.text() == "6" and self.btn1.text() == "1":

            self.different()

        elif self.btn6.text() == "6" and self.btn2.text() == "2":

            self.different()

        elif self.btn6.text() == "6" and self.btn7.text() == "7":

            self.different()

        elif self.btn6.text() == "6" and self.btn8.text() == "8":

            self.different()

    def Btn7(self):

        self.btn7.setStyleSheet("background-color:gray")
        self.btn7.setText("7")
        self.counter4 +=1

        if self.btn7.text() == "7" and self.btn8.text() == "8" :
            self.btn7.setStyleSheet("background-color:gray")
            self.btn8.setStyleSheet("background-color:gray")
            self.btn1.setStyleSheet("background-color:black")
            self.btn5.setStyleSheet("background-color:black")
            self.btn6.setStyleSheet("background-color:black")
            self.btn2.setStyleSheet("background-color:black")
            self.btn3.setStyleSheet("background-color:black")
            self.btn4.setStyleSheet("background-color:black")

            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn7.setVisible(False)
            self.btn8.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn2.setText("")
            self.btn4.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.check()



        elif self.btn7.text() == "7" and self.btn1.text() == "1" :

            self.different()

        elif self.btn7.text() == "7" and self.btn2.text() == "2":

            self.different()


        elif self.btn7.text() == "7" and self.btn3.text() == "3":

            self.different()

        elif self.btn7.text() == "7" and self.btn4.text() == "4":


            self.different()




        elif self.btn7.text() == "7" and self.btn5.text() == "5":

            self.different()

        elif self.btn7.text() == "7" and self.btn6.text() == "6":

            self.different()

    def Btn8(self):

        self.btn8.setStyleSheet("background-color:gray")
        self.btn8.setText("8")
        self.counter4 += 1

        if self.btn8.text() == "8" and self.btn7.text() == "7":
            self.btn7.setStyleSheet("background-color:gray")
            self.btn8.setStyleSheet("background-color:gray")
            self.btn1.setStyleSheet("background-color:black")
            self.btn5.setStyleSheet("background-color:black")
            self.btn6.setStyleSheet("background-color:black")
            self.btn2.setStyleSheet("background-color:black")
            self.btn3.setStyleSheet("background-color:black")
            self.btn4.setStyleSheet("background-color:black")

            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn7.setVisible(False)
            self.btn8.setVisible(False)
            self.score += 1
            self.label2.setText(str(self.score))
            self.btn1.setText("")
            self.btn3.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn2.setText("")
            self.btn4.setText("")
            self.btn7.setText("")
            self.btn8.setText("")

            self.check()


        elif self.btn8.text() == "8" and self.btn1.text() == "1":

            self.different()

        elif self.btn8.text() == "8" and self.btn2.text() == "2":

            self.different()


        elif self.btn8.text() == "8" and self.btn3.text() == "3":

            self.different()

        elif self.btn8.text() == "8" and self.btn4.text() == "4":

            self.different()

        elif self.btn8.text() == "8" and self.btn5.text() == "5":
            self.different()


        elif self.btn8.text() == "8" and self.btn6.text() == "6":

            self.different()










if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()