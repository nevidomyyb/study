from typing import Optional
from node import Node

class Stack:
    
    def __init__(self, top: Optional['Node'] = None, len = 0) -> None:
        self.top = top
        self.len = 0 if top is None else 1
        
    def __len__(self) -> int:
        return self.len

    def isEmpty(self) -> bool:
        return len(self) == 0  
    
    def getTop(self) -> Optional[Node]:
        if self.isEmpty(): return None
        
        return self.top

    def push(self, node: Node) -> None:
        if self.isEmpty(): 
            self.top = node
        else:
            node.setNext(self.top)
            self.top = node
        self.len +=1
        
    def pop(self) -> Node:
        if self.isEmpty():
            print("Stack is empty")
            return None
        temp = self.top
        self.top = temp.getNext()
        return temp
    
    def print(self) -> None:
        if len(self) == 0:
            print("Stack is empty")
            return None
        node = self.top
        while node != None:
            print(node.getValue())
            node = node.getNext()
    