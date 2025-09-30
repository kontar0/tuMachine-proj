from .Function import Function

class DeleteWordBeforeSymbol(Function):
    def __init__(self, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol)

    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def buildInit(self, startState):
        return super().buildInit(startState)
    
    def startCycle(self, change=None, rank=2):
        return super().startCycle(change, rank)
    
    def build(self, alphabet: str, startState: int) -> str:
        self.buildInit(startState)
        self.code(" ",self.specSymbol,startState=self.startState)
        self.code(self.specSymbol,0,1)
        self.code(alphabet,0)
        self.code(" ",1,1)
        self.code(alphabet," ")
        self.code(" ",1)
        self.code(self.specSymbol,0,endState=self.endState)
        return self.tuCode