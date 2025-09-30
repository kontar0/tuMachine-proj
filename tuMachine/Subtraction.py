from .Function import Function

class Subtraction(Function):
    def __init__(self, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol)

    def buildInit(self, startState):
        return super().buildInit(startState)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def startCycle(self, change=None, rank=2):
        return super().startCycle(change, rank)
    
    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)
    
    def build(self, alphabet: str, startState: int) -> str:
        self.buildInit(startState)
        self.startCycle(1)
        self.code(" ",0,0,self.startState,self.startOfCycle)
        for x in alphabet[1:]:
            print(x, str(int(x)-1))
            self.code(x,str(int(x)-1),startState=self.startOfCycle,endState=self.endOfCycle)
        self.code(alphabet[0],0,startState=self.startOfCycle,endState=self.startOfCycle)
        self.code(" "," ",startState=self.startOfCycle,endState=self.endState())
        self.code(alphabet,1,1,startState=self.endOfCycle)
        self.startCycle(1)
        self.code(alphabet,1,1,endState=self.endState())
        self.code(alphabet,alphabet[-1],1,self.startOfCycle)
        self.code(alphabet,1,1)
        self.code(" ",2,endState=self.startState(1))
        self.code(alphabet,2,endState=self.startOfCycle)

        return self.tuCode