# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 733)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 450, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.display.setFont(font)
        self.display.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.display.setStyleSheet("color: rgb(238, 238, 236);\n"
"background-color: rgb(136, 138, 133);")
        self.display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.display.setObjectName("display")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(10, 90, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b1.setFont(font)
        self.b1.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(186, 189, 182);")
        self.b1.setObjectName("b1")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(10, 190, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b4.setFont(font)
        self.b4.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b4.setObjectName("b4")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(110, 290, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b8.setFont(font)
        self.b8.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b8.setObjectName("b8")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(10, 290, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b7.setFont(font)
        self.b7.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(186, 189, 182);\n"
"")
        self.b7.setObjectName("b7")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(110, 190, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b5.setFont(font)
        self.b5.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b5.setObjectName("b5")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(110, 90, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b2.setFont(font)
        self.b2.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b2.setObjectName("b2")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(110, 390, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b0.setFont(font)
        self.b0.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b0.setObjectName("b0")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(210, 190, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b6.setFont(font)
        self.b6.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b6.setObjectName("b6")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(210, 90, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b3.setFont(font)
        self.b3.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(186, 189, 182);")
        self.b3.setObjectName("b3")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(210, 290, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.b9.setFont(font)
        self.b9.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.b9.setObjectName("b9")
        self.bEqual = QtWidgets.QPushButton(self.centralwidget)
        self.bEqual.setGeometry(QtCore.QRect(350, 590, 90, 135))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bEqual.setFont(font)
        self.bEqual.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(164, 0, 0);")
        self.bEqual.setObjectName("bEqual")
        self.bMulti = QtWidgets.QPushButton(self.centralwidget)
        self.bMulti.setGeometry(QtCore.QRect(310, 290, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bMulti.setFont(font)
        self.bMulti.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bMulti.setObjectName("bMulti")
        self.bMinus = QtWidgets.QPushButton(self.centralwidget)
        self.bMinus.setGeometry(QtCore.QRect(310, 190, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bMinus.setFont(font)
        self.bMinus.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bMinus.setObjectName("bMinus")
        self.bPlus = QtWidgets.QPushButton(self.centralwidget)
        self.bPlus.setGeometry(QtCore.QRect(310, 90, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bPlus.setFont(font)
        self.bPlus.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bPlus.setObjectName("bPlus")
        self.bDiv = QtWidgets.QPushButton(self.centralwidget)
        self.bDiv.setGeometry(QtCore.QRect(310, 390, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bDiv.setFont(font)
        self.bDiv.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bDiv.setObjectName("bDiv")
        self.bDiv2 = QtWidgets.QPushButton(self.centralwidget)
        self.bDiv2.setGeometry(QtCore.QRect(310, 490, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bDiv2.setFont(font)
        self.bDiv2.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bDiv2.setObjectName("bDiv2")
        self.bRem = QtWidgets.QPushButton(self.centralwidget)
        self.bRem.setGeometry(QtCore.QRect(10, 630, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bRem.setFont(font)
        self.bRem.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bRem.setObjectName("bRem")
        self.bExp = QtWidgets.QPushButton(self.centralwidget)
        self.bExp.setGeometry(QtCore.QRect(160, 630, 135, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bExp.setFont(font)
        self.bExp.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bExp.setObjectName("bExp")
        self.bSqrt = QtWidgets.QPushButton(self.centralwidget)
        self.bSqrt.setGeometry(QtCore.QRect(20, 490, 270, 135))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bSqrt.setFont(font)
        self.bSqrt.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bSqrt.setObjectName("bSqrt")
        self.bSqrt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bSqrt_2.setGeometry(QtCore.QRect(210, 390, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bSqrt_2.setFont(font)
        self.bSqrt_2.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bSqrt_2.setObjectName("bSqrt_2")
        self.bSqrt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bSqrt_3.setGeometry(QtCore.QRect(10, 390, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.bSqrt_3.setFont(font)
        self.bSqrt_3.setStyleSheet("color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);")
        self.bSqrt_3.setObjectName("bSqrt_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.application()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        MainWindow.setWindowIcon(QIcon('icon.jpg'))
        self.display.setText(_translate("MainWindow", "0"))
        self.b1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>background-color: rgb(46, 52, 54);</p></body></html>"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.bEqual.setText(_translate("MainWindow", "="))
        self.bMulti.setText(_translate("MainWindow", "*"))
        self.bMinus.setText(_translate("MainWindow", "-"))
        self.bPlus.setText(_translate("MainWindow", "+"))
        self.bDiv.setText(_translate("MainWindow", "/"))
        self.bDiv2.setText(_translate("MainWindow", "//"))
        self.bRem.setText(_translate("MainWindow", "%"))
        self.bExp.setText(_translate("MainWindow", "**"))
        self.bSqrt.setText(_translate("MainWindow", "Clear"))
        self.bSqrt_2.setText(_translate("MainWindow", "delete"))
        self.bSqrt_3.setText(_translate("MainWindow", "."))


    def application(self):
        self.b0.clicked.connect(lambda: self.write(self.b0.text()))
        self.b1.clicked.connect(lambda: self.write(self.b1.text()))
        self.b2.clicked.connect(lambda: self.write(self.b2.text()))
        self.b3.clicked.connect(lambda: self.write(self.b3.text()))
        self.b4.clicked.connect(lambda: self.write(self.b4.text()))
        self.b5.clicked.connect(lambda: self.write(self.b5.text()))
        self.b6.clicked.connect(lambda: self.write(self.b6.text()))
        self.b7.clicked.connect(lambda: self.write(self.b7.text()))
        self.b8.clicked.connect(lambda: self.write(self.b8.text()))
        self.b9.clicked.connect(lambda: self.write(self.b9.text()))
        self.bPlus.clicked.connect(lambda: self.write(self.bPlus.text()))
        self.bMinus.clicked.connect(lambda: self.write(self.bMinus.text()))
        self.bMulti.clicked.connect(lambda: self.write(self.bMulti.text()))
        self.bDiv.clicked.connect(lambda: self.write(self.bDiv.text()))
        self.bDiv2.clicked.connect(lambda: self.write(self.bDiv2.text()))
        self.bRem.clicked.connect(lambda: self.write(self.bRem.text()))
        self.bExp.clicked.connect(lambda: self.write(self.bExp.text()))
        self.bSqrt.clicked.connect(lambda: self.display.setText('0'))
        self.bEqual.clicked.connect(self.result)
        self.bSqrt_2.clicked.connect(lambda: self.display.setText(self.display.text()[:-1]))
        self.bSqrt_3.clicked.connect(lambda: self.write(self.bSqrt_3.text()))

    def write(self, value):
        if self.display.text() == '0' and value != '+' and value != '-' and value != '*' and value != '**' and value != '/' and value != '//' and value != '%':
            self.display.setText(value)
        else:
            self.display.setText(self.display.text() + value)

    def result(self):
        res = eval(self.display.text())
        self.display.setText(str(res))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
