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


class Sessions:
    def __init__(self, sessionNum, HIITround1, GVT1, HIITround2, GVT2, ):
        self.sessionNum = sessionNum
        self.HIITround1 = HIITround1
        self.GVT1 = GVT1
        self.HIITround2 = HIITround2
        self.GVT2 = GVT2
        
    def printShit(self):
        print(self.sessionNum, self.HIITround1, self.GVT1, self.HIITround2, self.GVT2)
        


