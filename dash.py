
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, Qt, QThreadPool
import pandas as pd
from time import sleep

bookDf = pd.read_csv("book.csv")

class Runnable(QRunnable):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global bookDf
        self.main(bookDf, 1)

        # while True:
        #     self.textInputText = ui.textInput.toPlainText()
        #     if "\n" in self.textInputText:
        #         print(self.textInputText)
        #         ui.textInput.setPlainText("")
        #         self.textInputText = ""
                
        #     
                
                
    def sessionSetup(self, bookDf, sessionNum, weekContents):
        HIIT = []
        GVT = []
        a = weekContents[2].split(",")
        if "HIIT" in a: HIIT.append(a)
        else: GVT.append(a)
        b = weekContents[3].split(",")
        if "HIIT" in b: HIIT.append(b)
        else: GVT.append(b)
        c = weekContents[4].split(",")
        if "HIIT" in c: HIIT.append(c)
        else: GVT.append(c)
        d = weekContents[5].split(",")
        if "HIIT" in d: HIIT.append(d)
        else: GVT.append(d)
        print("Welcome to Session {seshNum}. This week we will be covering {desc}. For GVT, you have the option for {GVT1a} and {GVT1b} for the first section and {GVT2a} and {GVT2b} for second section.".format(seshNum = sessionNum, desc = weekContents[1], GVT1a = GVT[0][0], GVT1b = GVT[0][1], GVT2a = GVT[1][0], GVT2b = GVT[1][1]))
        choices = input("Please enter in the form firstChoice,secondChoice: ")
        
        # update the dataFrame to reflect the user's choices.
        bookDf.at[sessionNum - 1,"uBChoice"] = GVT[0][int(choices[0])-1]
        bookDf.at[sessionNum - 1, "uDChoice"] = GVT[1][int(choices[2])-1]
        bookDf.to_csv("book.csv", index=False)

    
        print("You have chosen {one} and {two}.".format(one = GVT[0][int(choices[0])-1], two = GVT[1][int(choices[2])-1]))
        return a,b,c,d,HIIT,GVT,choices

    def progressBarHIIT(self, stage):
        self.activeProgressBar = 0
        self.restProgressBar = 0
        
        for i in range(int(stage[1])):
            print("GO")
            self.restProgressBar = 0
            for j in range(int(0.1)): #stage[2]
                self.activeProgressBar = round(100/int(0.1) * j) # stage[2]
                ui.progressBar.setValue(self.activeProgressBar)
                print(self.activeProgressBar)
                sleep(1)
                
            self.activeProgressBar = 0
            print("REST. {sets} active sets remaining.".format(sets = int(stage[1]) - i - 1))
            for k in range(int(0.1)): #stage[3]
                self.restProgressBar = round(100/int(0.1) * k) # stage[3]
                ui.progressBar.setValue(self.restProgressBar)
                print(self.restProgressBar)
                sleep(1)
        return True
        

    def main(self, bookDf, sessionNum):
        weekContents = bookDf.loc[sessionNum-1,:] # locating a specific row.
        a,b,c,d,HIIT,GVT,choices = self.sessionSetup(bookDf, sessionNum, weekContents)
        
        ui.output.setText("HIIT round 1. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes. Press Enter to start".format(sets = a[1], dur = a[2], durR = a[3], restFin = a[4]))

        if self.progressBarHIIT(a) == True: print("FINISH")

        print("Time for GVT. First up is {exercise}. Perform {sets} sets of {reps} reps.".format(exercise = GVT[0][int(choices[0])-1], sets = b[2], reps = b[3]))

        input("Press Enter when you've finished.")
        
        print("HIIT round 2. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes.".format(sets = c[1], dur = c[2], durR = c[3], restFin = c[4]))
        input("Press Enter to start")
        if self.progressBarHIIT(c) == True: print("FINISH")
        
        print("Time for GVT. First up is {exercise}. Perform {sets} sets of {reps} reps.".format(exercise = GVT[1][int(choices[2])-1], sets = d[2], reps = d[3]))

        input("Press Enter when you've finished.")
        
        
    def csvResetFunc(bookDf):    
        for i in range(len(bookDf["uAChoice"])):
            bookDf.at[i, "uAChoice"] = "n"
            
        for i in range(len(bookDf["uBChoice"])):
            bookDf.at[i, "uBChoice"] = "n"
            
        for i in range(len(bookDf["uCChoice"])):
            bookDf.at[i, "uCChoice"] = "n"
            
        for i in range(len(bookDf["uDChoice"])):
            bookDf.at[i, "uDChoice"] = "n"
    
        bookDf.to_csv("book.csv", index=False)
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 459, 500, 91))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 791, 311))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setGeometry(QtCore.QRect(0, 10, 16, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(10, 180, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(10, 240, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(200, 10, 16, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(10, 120, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(10, 300, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 0, 780, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_8 = QtWidgets.QFrame(self.widget)
        self.line_8.setGeometry(QtCore.QRect(780, 10, 16, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setObjectName("line_8")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(240, 130, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(240, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(240, 250, 191, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setGeometry(QtCore.QRect(10, 70, 781, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy)
        self.line_10.setStyleSheet("color: rgb(255, 255, 0)")
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(70)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.widget)
        self.line_11.setGeometry(QtCore.QRect(10, 190, 781, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy)
        self.line_11.setStyleSheet("color: rgb(255, 255, 0)")
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(70)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.line_11.raise_()
        self.line_10.raise_()
        self.line_8.raise_()
        self.line_7.raise_()
        self.line_9.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_3.raise_()
        self.line_2.raise_()
        self.line_6.raise_()
        self.line.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(200, 350, 400, 51))
        self.output.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.textInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(300, 410, 200, 31))
        self.textInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textInput.setPlainText("")
        self.textInput.setObjectName("textInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Training Description"))
        self.label_2.setText(_translate("MainWindow", "HIIT Round 1"))
        self.label_3.setText(_translate("MainWindow", "GVT"))
        self.label_4.setText(_translate("MainWindow", "HIIT Round 2"))
        self.label_5.setText(_translate("MainWindow", "GVT"))
        self.label_6.setText(_translate("MainWindow", "Guidelines"))
        self.label_7.setText(_translate("MainWindow", "n"))
        self.label_8.setText(_translate("MainWindow", "n"))
        self.label_9.setText(_translate("MainWindow", "n"))
        self.label_10.setText(_translate("MainWindow", "n"))
        self.output.setText(_translate("MainWindow", "Status"))

    def runTasks(self):
            threadCount = QThreadPool.globalInstance().maxThreadCount()
            pool = QThreadPool.globalInstance()
            runnable = Runnable()
            pool.start(runnable)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.runTasks()
    MainWindow.show()
    sys.exit(app.exec_())