from node import Node
from typing import Optional

class BinaryTree:
    
    def __init__(self, root: Node = None) -> None:
        self.root = root
        
    def getRoot(self) -> Node:
        return self.root    
    
    def insert(self, node: Node) -> None:
        insert_in = self.root
        # print(f"Trying insert: {node}")
        while True:
            # print(f"Analysing {insert_in}")
            if node.getValue() > insert_in.getValue():
                # print(f"Its higher than: {insert_in} going to right")
                if insert_in.getRight() is None:
                    insert_in.setRight(node)
                    break
                insert_in = insert_in.getRight()
            else:
                # print(f"Its lower than: {insert_in} going to left")
                if insert_in.getLeft() is None:
                    insert_in.setLeft(node)
                    break
                insert_in = insert_in.getLeft()
    
    def insertRecursive(self, node: Node, current: Optional[Node] = None) -> None:
        if current is None:
            current = self.getRoot()
        if node.getValue() > current.getValue():
            if current.getRight() is None:   current.setRight(node)
            else: self.insertRecursive(node, current.getRight())
        else:
            if current.getLeft() is None: current.setLeft(node)
            else: self.insertRecursive(node, current.getLeft())
    
    def search(self, value, current: Node) -> Optional[Node]:
        if current is None:
            return None
        if current.getValue() == value:
            return current
        if current.getValue() < value:
            return self.search(value, current.getRight())
        return self.search(value, current.getLeft())
    
    def lowestValue(self, node: Node) -> Node:
        current = node
        while current.getLeft() is not None:
            current = current.getLeft()
        return current

    def highestValue(self, node:Node) -> Node:
        current = node
        while current.getRight() is not None:
            current = current.getRight()
        return current
    
    def delete(self, value, current: Node) -> Node:
        if current is None:
            return None #Value not found in tree
        if value < current.getValue():
            current.setLeft(self.delete(value, current.getLeft()))
        elif value > current.getValue():
            current.setRight(self.delete(value, current.getRight()))
        else:
            if current.getLeft() is None:
                return  current.getRight()
            elif current.getRight() is None:
                return current.getLeft()
            temp = self.lowestValue(current.getRight())
            current.setValue(temp.getValue())
            current.setRight(self.delete(temp.getValue(), current.getRight()))
        return current
        
    def inOrderTransversal(self, node: Node) -> None:
        if node != None:
            self.inOrderTransversal(node.getLeft())
            print(node)
            self.inOrderTransversal(node.getRight())
        
            
            
        