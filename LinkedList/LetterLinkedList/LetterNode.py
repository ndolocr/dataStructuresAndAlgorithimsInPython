class LetterNode:
    def __init__(self, letter:str):
        self.letter = letter
        self.nextPointer = None

    # Set Letter
    def setLetter(self, letter:str):
        self.letter = letter
    
    # Get Letter
    def getLetter(self):
        return self.letter
    
    # Set Pointer to next Node
    def setNextPointer(self, nextPointer):
        self.nextPointer = nextPointer
    
    # Get next Pointer
    def getNextPointer(self):
        return self.nextPointer