from .Function import Function

class CopyThroughtBeforeRight(Function):
    def __init__(self, placeStopSymbol=0, elements=0, directionFrom=1, directionTo=0, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol)
        self.elements = elements
        self.directionFrom = directionFrom
        self.directionTo = directionTo
        self.placeStopSymbol = placeStopSymbol

    def buildInit(self, startState):
        return super().buildInit(startState)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)
    
    def build(self, alphabet: str, startState: int) -> str:
        self.buildInit(startState)
        self.startCycle(1)
        if self.placeStopSymbol:
            self.code(" ",self.directionFrom,1,startState=self.startState)
            self.code(alphabet,self.directionFrom)
            self.code(" ","$",1)
            self.code("$",self.directionTo,1)
            self.code(alphabet,self.directionTo)
            self.code(" ",self.directionFrom,1)
            self.code(alphabet,2,endState=self.startOfCycle)
        else:
            self.code(alphabet,2,self.startState,endState=self.startOfCycle)
        for x in alphabet:
            self.code(x," ",1,self.startOfCycle)
            self.code(" ",self.directionTo,1)
            self.code(" ",self.directionTo)
            self.code(alphabet,self.directionTo-1,1)
            self.code(" ",self.directionTo-1,1)
            self.code(" ",x)
            self.code(x,self.directionTo-1,1)
            self.code(" ",self.directionTo-1)
            self.code(alphabet,2,1,endState=self.endOfCycle)
        temp = self.endOfCycle
        self.startCycle(1)
        print(temp, self.startOfCycle)
        self.code(alphabet,2,1,temp,self.startOfCycle)
        for x in alphabet:
            self.code(x," ",1,startState=self.startOfCycle)
            self.code(" ",self.directionTo,1)
            self.code(" ",self.directionTo)
            self.code(alphabet,self.directionTo-1,1)
            self.code(" ",x)
            self.code(x,self.directionTo-1,1)
            self.code(" ",self.directionTo-1)
            self.code("$"," ",endState=self.endOfCycle)
            self.code(alphabet,2,endState=self.startOfCycle)
        self.code(" ",self.directionTo,1,startState=self.endOfCycle)
        self.code(" ",self.directionTo)
        self.code(alphabet,self.directionTo-1,endState=self.endState)
        return self.tuCode