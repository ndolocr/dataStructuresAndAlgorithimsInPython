class LetterLinkedList:
    def __init__(self, head):
        self.head = head
    
    def printLinkedList(self):
        currentNode = self.head
        output = ""

        while currentNode:
            output += f"{currentNode.letter} ---> "
            currentNode = currentNode.getNextPointer()
        output +=" Null"

        return output