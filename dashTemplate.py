
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
        activeProgressBar = 0
        restProgressBar = 0
        
        for i in range(int(stage[1])):
            print("GO")
            restProgressBar = 0
            for j in range(int(0.1)): #stage[2]
                activeProgressBar = round(100/int(0.1) * j) # stage[2]
                print(activeProgressBar)
                sleep(1)
                
            activeProgressBar = 0
            print("REST. {sets} active sets remaining.".format(sets = int(stage[1]) - i - 1))
            for k in range(int(0.1)): #stage[3]
                restProgressBar = round(100/int(0.1) * k) # stage[3]
                print(restProgressBar)
                sleep(1)
        return True
        

    def main(self, bookDf, sessionNum):
        weekContents = bookDf.loc[sessionNum-1,:] # locating a specific row.
        a,b,c,d,HIIT,GVT,choices = self.sessionSetup(bookDf, sessionNum, weekContents)
        
        print("HIIT round 1. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes.".format(sets = a[1], dur = a[2], durR = a[3], restFin = a[4]))
        input("Press Enter to start")
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