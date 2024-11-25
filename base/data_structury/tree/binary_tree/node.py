class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
    def setValue(self, value) -> None:
        self.value = value
    def getValue(self):
        return self.value
    def setLeft(self, left: 'Node') -> None:
        self.left = left
    def setRight(self, right: 'Node') -> None:
        self.right = right
    def getLeft(self) -> 'Node':
        return self.left
    def getRight(self) -> 'Node':
        return self.right