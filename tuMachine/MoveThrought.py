from .Function import Function

class MoveThrought(Function):

    def __init__(self, elements, direction: int, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol)
        self.elements = elements
        self.direction = direction

    direc = "<>"
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)

    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def startCycle(self, change, rank=2):
        return super().startCycle(change, rank)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def buildInit(self, startState):
        return super().buildInit(startState)

    def build(self, alphabet, startState,):
        self.buildInit(startState)
        self.code(" ",self.direction,1,self.startState)
        self.code(" ",self.direction)
        self.code(alphabet,2,1)
        for el in range(1, self.elements*2):
            if el%2!=0:
                self.code(alphabet,self.direction)
                self.code(" ",2 if el == self.elements * 2 - 1 else self.direction,1, endState=self.endState() if el == self.elements * 2 - 1 else None)
            else:
                self.code(" ",self.direction)
                self.code(alphabet,self.direction-1)
                self.code(" ",self.direction,1)
        return self.tuCode
