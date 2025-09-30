from .CopySymbol import CopySymbol
from .Function import Function
from .MoveThrought import MoveThrought

class CopyThrought(Function):
    def __init__(self, elements, directionFrom, directionTo, rank=4, specSymbol="$"):
        super().__init__(rank, specSymbol) 
        self.elements = elements
        self.directionFrom = directionFrom
        self.directionTo = directionTo

    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)
    
    def endState(self, change=None) -> int:
        return super().endState(change)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)
    
    def buildInit(self, startState):
        return super().buildInit(startState)
    
    def build(self, alphabet: str, startState) -> str:
        self.buildInit(startState)
        if self.directionFrom == 1:
            self.code(" ",self.directionFrom,0,self.startState,self.startState)
            self.code(alphabet,self.directionFrom-1,1,self.startState)
            self.code(" ",self.directionFrom,1,endState=self.endState())
            copy = CopySymbol(self.elements,self.directionTo)
            self.tuCode += copy.build(alphabet, self.endState())
            self.uses += copy.uses
            self.endState(1)
            self.code(alphabet,self.directionFrom,1,startState=copy.endState())
            self.code(alphabet,2,0,endState=copy.startState)
            self.code(" ",2,endState=self.endState())
        else:
            self.code(" ",self.directionFrom,1,self.startState)
            self.code(alphabet,self.directionFrom)
            self.code(" ",self.directionFrom-1,1)

            self.code(" ",self.directionFrom-1,0)
            self.code(alphabet,self.directionFrom,1)
            self.code(" ",self.directionFrom-1,1,endState=self.endState())
            copy = CopySymbol(self.elements,self.directionTo)
            self.tuCode += copy.build(alphabet, self.endState())
            self.uses += copy.uses
            self.endState(1)
            self.code(alphabet,self.directionFrom-1,1,startState=copy.endState())
            self.code(alphabet,2,0,endState=copy.startState)
            self.code(" ",2,endState=self.endState())
        return self.tuCode
