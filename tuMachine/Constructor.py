from os.path import exists
from os import remove
from string import digits, ascii_uppercase

class Constructor():
	alpha = digits + ascii_uppercase

	def __init__(self, functions: list, power: int):
		self.alpha = self.alpha[:power]
		self.code = "00, ,=,1"
		c=0
		for x in functions:
			c+=1
			if c == 1:
				self.code += x.build(str(self.alpha),1)
				self.endState = x.endState()
			else:
				self.code += x.build(str(self.alpha),self.endState)
				self.endState = x.endState()
		self.code += f"\n{self.endState}, , ,{self.endState}"

	def build(self, name):
		if exists(name):
			remove("./" + name)
		file = open(name, "w+")
		file.write(self.code)
		file.close 