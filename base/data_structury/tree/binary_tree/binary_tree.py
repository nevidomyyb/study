from node import Node


class BinaryTree:
    
    def __init__(self, root: Node) -> None:
        self.root = root
        
    def getRoot(self) -> Node:
        return self.root
    
    def insert(self, parent: Node, child: Node, orientation: str) -> None:
        if orientation == "e":
            parent.setLeft(child)
        else:
            parent.setRight(child)
    
    def preOrderTransversal(self, node: Node):
        if node != None:
            print(node.getValue())
            self.preOrderTransversal(node.getLeft())
            self.preOrderTransversal(node.getRight())
            
    def postOrderTransversal(self, node: Node):
        if node != None:
            self.postOrderTransversal(node.getLeft())
            self.postOrderTransversal(node.getRight())
            print(node.getValue())
            