from node import Node
from typing import Optional

class Queue:
    
    def __init__(self) -> None:
        self.len = 0
        self.head = None
        self.tail = None
    
    def __len__(self) -> int:
        return self.len
    
    def isEmpty(self) -> bool:
        return (self.len == 0)
    
    def enqueue(self, node: Node) -> None:
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node
        self.len += 1
        
    def dequeue(self) -> Optional[Node]:
        if self.isEmpty():
            return None
        temp = self.head
        self.head = temp.getNext()
        self.len -= 1
        return temp

    def getPeek(self) -> Optional[Node]:
        return self.head
    
    def print(self) -> None:
        element = self.head
        print('Head', end='')
        while element != None:
            print(f" {element.getValue()} ", end='')
            element = element.getNext()
        print('Tail')
        
