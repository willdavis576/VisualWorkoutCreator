'''
Sessions <- class container?
    block of 4 sections
        cardio
            how many sets?
            duration of each set?
            rest between?
            rest when finished?
        weights
            choice of activity - just a number i guess
        cardio
            ditto all before
        weights
            ditto all before
            
Saving is required, as well as tracking progress.

'''

from time import sleep


# class Sessions:
#     def __init__(self, sessionNum, HIITround1, GVT1, HIITround2, GVT2):
#         self.sessionNum = sessionNum
#         self.HIITround1 = HIITround1
#         self.GVT1 = GVT1
#         self.HIITround2 = HIITround2
#         self.GVT2 = GVT2
        
#     def printShit(self):
#         print(self.sessionNum, self.HIITround1, self.GVT1, self.HIITround2, self.GVT2)
        

# #i knowwwww eval on input is bad, shut up, it's temporary.
# sessionNum = 1 #int(input("insert your session number. "))
# HIITround1 = (6,35,45,2) #eval(input("insert: sets amount, set duration, set rest, final rest "))
# GVT1 = (1,10,10) #eval(input("insert: activity 1 or 2, sets amount, reps amount "))
# HIITround2 = (6,35,45,2) #eval(input("insert: sets amount, set duration, set rest, final rest "))
# GVT2 = (1,10,10) #eval(input("insert: activity 1 or 2, sets amount, reps amount "))

# session = Sessions(sessionNum, HIITround1, GVT1, HIITround2, GVT2)
# session.printShit()

'''
I need to write some sort of empty framework than can be populated and displayed on screen
maybe QT?
'''

import pandas as pd

bookDf = pd.read_csv("book.csv")

def sessionSetup(bookDf, sessionNum, weekContents):
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
    print("Welcome to Session {seshNum}. This week we will be covering {desc}. For GVT, you have the option for {GVT} for the first section and {GVT2} for second section.".format(seshNum = sessionNum, desc = weekContents[1], GVT= GVT[0], GVT2 = GVT[1]))
    choices = input("Please enter in the form firstChoice,secondChoice: ")
    print("You have chosen {one} and {two}.".format(one = GVT[0][int(choices[0])-1], two = GVT[1][int(choices[2])-1]))
    return a,b,c,d,HIIT,GVT

def main2(bookDf, sessionNum):
    weekContents = bookDf.loc[sessionNum-1,:]
    a,b,c,d,HIIT,GVT = sessionSetup(bookDf, sessionNum, weekContents)
    
    countDown = 3
    activeProgressBar = 0
    restProgressBar = 0
    
    sleep(0.1) 
    
    for i in range(3):
        print(countDown)
        countDown -= 1
        sleep(1)
    
    stage = a
    print("HIIT round 1. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes.".format(sets = stage[1], dur = stage[2], durR = stage[3], restFin = stage[4]))
    
    # Display the visual prgression bar now and maybe the picture of the exercise??????
    for i in range(int(stage[1])):
        print("GO")
        restProgressBar = 0
        for j in range(int(stage[2])):
            activeProgressBar = round(100/int(stage[2]) * j)
            print(activeProgressBar)
            sleep(1)
            
        activeProgressBar = 0
        print("REST. {sets} active sets remaining.".format(sets = int(stage[1]) - i - 1))
        for k in range(int(stage[3])):
            restProgressBar = round(100/int(stage[3]) * k)
            print(restProgressBar)
            sleep(1)
            
    
    

main2(bookDf, 1)



def main(session):
    step = 0
    
    if step == 0:
        print("HIIT Round 1. {sets} sets of {setDur} seconds with a {setRest} second rest between sets. At the end, rest for {finalRest}".format(sets = session.HIITround1[0], setDur = session.HIITround1[1], setRest = session.HIITround1[2], finalRest = session.HIITround1[3]))
        input("Press Enter when you're ready to start.")
        countDown = 3
        activeProgressBar = 0
        restProgressBar = 0
        
        sleep(0.1) 
        for i in range(3):
            print(countDown)
            countDown -= 1
            sleep(1)
        print("GO")
        print("Jogging for {setDur} seconds".format(setDur = session.HIITround1[1]))
        
        # Display the visual prgression bar now and maybe the picture of the exercise??????
        for i in range(session.HIITround1[0]):
            for j in range(session.HIITround1[1]):
                activeProgressBar = round(100/session.HIITround1[1] * j)
                print(activeProgressBar)
                sleep(1)
                
            activeProgressBar = 0
            
            for k in range(session.HIITround1[2]):
                restProgressBar = round(100/session.HIITround1[2] * k)
                print(restProgressBar)
                sleep(1)
            
        

    
    
    
    
    
# main(session)