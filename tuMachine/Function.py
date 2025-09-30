class Function():
    def __init__(self, rank=4, specSymbol="$"):
        self.idx = 0
        self.uses = 1
        self.rank = rank
        self.specSymbol=specSymbol
        self.states = [0 for i in range(rank)]
        self.currState = f"!{"".join(map(str, self.states))}"
        self.tuCode = ''

    def endState(self, change=None) -> int:
        if change:
            self.uses += change
        return self.states[1] + self.uses
    
    def changeState(self, rank, change=None) -> str:
        if change: 
            self.states[rank] += 1
            self.currState = f"!{"".join(map(str, self.states))}"
        return self.currState
    
    def startCycle(self, change=None, rank=2):
        self.startOfCycle = self.changeState(rank)
        self.endOfCycle = self.changeState(rank, change)
    
    def code(self, condition: str, action, change=None, startState=None, endState=None):
        start = startState if startState else self.currState
        end = endState if endState else self.changeState(0,change)
        for x in condition:
            self.tuCode += f"\n{start},{x},{"<>"[action] if action in [0, 1, -1] else "<>=#"[action] if action in [2, 3] else action},{end}"

    def buildInit(self, startState):
        self.startState = startState
        self.states[1] = startState
        self.currState = f"!{"".join(map(str, self.states))}"

    def build(self, alphabet: str, startState: int) -> str:
        self.buildInit(startState)
        self.alphabet = alphabet
        return self.tuCode
