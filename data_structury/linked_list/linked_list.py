from node import Node
from typing import Optional

class LinkedList:
    
    def __init__(self, head: Optional['Node']=None, len: int=0):
        self.head = head
        self.len = 0 if head is None else 1
    
    def addStart(self, node: 'Node') -> None:
        node.setNext(self.head)
        self.head = node
        self.len += 1
    
    def addEnd(self, node: 'Node') -> None:
        node.setNext(None)
        last = self.head
        while (last.getNext() != None):
            last = last.getNext()
        last.setNext(node)        
        self.len += 1
    
    def removeStart(self) -> bool:
        #If the Linekd List is empty, return False
        if self.head is None:
            return False
        
        old_head = self.head
        self.head = old_head.getNext()
        old_head.setNext(None)
        self.len -= 1
        return True
    
    def removeEnd(self):
        i = 1
        remove = self.head
        while (i < self.len):
            if (i == (self.len - 1)):
                remove.setNext(None)
                self.len -= 1
            remove = remove.getNext()
            i+=1
            
    def remove(self, position: int) -> Node:
        remove = self.head
        i = 1
        if position == 0:
            node = self.head
            self.removeStart()
            return node
        while (position <= self.len):
            if (position == i):
                temp = remove.getNext().getNext()
                remove.getNext().setNext(None)
                remove.setNext(temp)
                self.len -= 1
                break
            remove = remove.getNext()
            i+=1
            
    def add(self, position: int, node: Node) -> None:
        i = 1
        add_after = self.head
        if position == 0:
            self.addStart(node)
            return None
        while position <= self.len:
            if position == i:
                node.setNext(add_after.getNext())
                add_after.setNext(node)
                self.len += 1
                break
            add_after = add_after.getNext()
            i += 1
    
    def print(self) -> None:
        node = self.head
        if self.len == 0:
            print("Empty List")
        while (node != None):
            print(f" {node.getValue()}", end="")
            node = node.getNext()
        print()
    
