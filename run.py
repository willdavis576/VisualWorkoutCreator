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
    print("Welcome to Session {seshNum}. This week we will be covering {desc}. For GVT, you have the option for {GVT1a} and {GVT1b} for the first section and {GVT2a} and {GVT2b} for second section.".format(seshNum = sessionNum, desc = weekContents[1], GVT1a = GVT[0][0], GVT1b = GVT[0][1], GVT2a = GVT[1][0], GVT2b = GVT[1][1]))
    choices = input("Please enter in the form firstChoice,secondChoice: ")
    
    # update the dataFrame to reflect the user's choices.
    bookDf.at[sessionNum - 1,"uBChoice"] = GVT[0][int(choices[0])-1]
    bookDf.at[sessionNum - 1, "uDChoice"] = GVT[1][int(choices[2])-1]
    bookDf.to_csv("book.csv", index=False)

   
    print("You have chosen {one} and {two}.".format(one = GVT[0][int(choices[0])-1], two = GVT[1][int(choices[2])-1]))
    return a,b,c,d,HIIT,GVT,choices

def progressBarHIIT(stage):
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
    

def main(bookDf, sessionNum):
    weekContents = bookDf.loc[sessionNum-1,:] # locating a specific row.
    a,b,c,d,HIIT,GVT,choices = sessionSetup(bookDf, sessionNum, weekContents)
    
    print("HIIT round 1. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes.".format(sets = a[1], dur = a[2], durR = a[3], restFin = a[4]))
    input("Press Enter to start")
    if progressBarHIIT(a) == True: print("FINISH")

    print("Time for GVT. First up is {exercise}. Perform {sets} sets of {reps} reps.".format(exercise = GVT[0][int(choices[0])-1], sets = b[2], reps = b[3]))

    input("Press Enter when you've finished.")
    
    print("HIIT round 2. {sets} sets of {dur} seconds with a {durR} second rest between sets. Rest {restFin} minutes.".format(sets = c[1], dur = c[2], durR = c[3], restFin = c[4]))
    input("Press Enter to start")
    if progressBarHIIT(c) == True: print("FINISH")
    
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

main(bookDf, 1)
# csvResetFunc(bookDf)