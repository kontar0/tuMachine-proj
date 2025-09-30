from .Function import Function
from .MoveThrought import MoveThrought

class CopySymbol(Function):
	def __init__(self, elements, direction: int, rank=4, specSymbol="$"):
		super().__init__(rank, specSymbol)
		self.elements = elements
		self.direction = direction
				
	def code(self, condition: str, action, change=None, startState=None, endState=None):
		return super().code(condition, action, change, startState, endState)
	
	def endState(self, change=None) -> int:
		return super().endState(change)
	
	def changeState(self, rank, change=None) -> str:
		return super().changeState(rank, change)
	
	def startCycle(self, change=None, rank=2):
		return super().startCycle(change, rank)
	
	def buildInit(self, startState):
		return super().buildInit(startState)
	
	def build(self, alphabet, startState):
		self.buildInit(startState)
		self.startCycle(1)
		self.code(alphabet,2,0,self.startState,self.startOfCycle)
		for x in alphabet:
			self.code(x," ",1,self.startOfCycle)
			# self.code(self.specSymbol,2,self.startOfCycle,self.endState())
			for i in range(self.elements):
				self.code(" ",self.direction,1)
				self.code(alphabet,self.direction)
				if i != self.elements-1 or self.elements == 1:
					self.code(" ",self.direction,1)
					self.code(alphabet,self.direction)
			self.code(" ",x,1)
			for i in range(self.elements):
				self.code(alphabet,self.direction-1)
				self.code(" ",self.direction-1,1)
				self.code(alphabet,self.direction-1)
			self.code(" ",x,1,endState=self.endOfCycle)
		self.code(alphabet,2,0,self.endOfCycle,self.endState())
		return self.tuCode