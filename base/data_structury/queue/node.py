class Node:
    
    def __init__(self, value, next_=None) -> None:
        self.value = value
        self.next = next_
        
    def setValue(self, value) -> None:
        self.value = value
    def setNext(self, next_) -> None:
        self.next = next_
    def getValue(self):
        return self.value
    def getNext(self) -> 'Node':
        return self.next
    
