from .Function import Function

class Sdvig(Function):
    def __init__(self, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol)

    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)
    
    def buildInit(self, startState):
        return super().buildInit(startState)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def startCycle(self, change=None, rank=2):
        return super().startCycle(change, rank)
    
    def build(self, alphabet: str, startState: int) -> str:
        self.buildInit(startState)
        self.code(" ",1,1,self.startState)
        self.code(alphabet,alphabet)
        return self.tuCode