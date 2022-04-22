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


class Sessions:
    def __init__(self, sessionNum, HIITround1, GVT1, HIITround2, GVT2):
        self.sessionNum = sessionNum
        self.HIITround1 = HIITround1
        self.GVT1 = GVT1
        self.HIITround2 = HIITround2
        self.GVT2 = GVT2
        
    def printShit(self):
        print(self.sessionNum, self.HIITround1, self.GVT1, self.HIITround2, self.GVT2)
        

#i knowwwww eval on input is bad, shut up, it's temporary.
sessionNum = 1 #int(input("insert your session number. "))
HIITround1 = (6,35,45,2) #eval(input("insert: sets amount, set duration, set rest, final rest "))
GVT1 = (1,10,10) #eval(input("insert: activity 1 or 2, sets amount, reps amount "))
HIITround2 = (6,35,45,2) #eval(input("insert: sets amount, set duration, set rest, final rest "))
GVT2 = (1,10,10) #eval(input("insert: activity 1 or 2, sets amount, reps amount "))

session = Sessions(sessionNum, HIITround1, GVT1, HIITround2, GVT2)
session.printShit()

'''
I need to write some sort of empty framework than can be populated and displayed on screen
maybe QT?
'''

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
        for i in range(session.HITTround1[0]):
            for j in range(session.HIITround1[1]):
                activeProgressBar = 100/session.HIITround1[1] * j
                sleep(1)
                
            activeProgressBar = 0
            
            for k in range(session.HITTround1[2]):
                restProgressBar = 100/session.HITTround1[2] * k
                sleep(1)
            
        

    
    
    
    
    
main(session)