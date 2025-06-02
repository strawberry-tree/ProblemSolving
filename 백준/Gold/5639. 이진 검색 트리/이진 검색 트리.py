import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
    def find(self, x):
        curr = self.root
        while curr is not None:
            if x < curr.value:
                curr = curr.left
            elif x > curr.value:
                curr = curr.right
            elif x == curr.value:
                return True
        return False

    
    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            
        curr = self.root
        while curr is not None:
            parent = curr
            if x < curr.value:
                is_left = True
                curr = curr.left
            elif x > curr.value:
                is_left = False
                curr = curr.right
            elif x == curr.value:
                return False
        
        if is_left:
            parent.left = Node(x)
        else:
            parent.right = Node(x)
 
tree = Tree()
while True:
    try:
        x = int(input())
        tree.insert(x)
    except:
        break

def postorder(tree, node):
    if node is not None:
        postorder(tree, node.left)
        postorder(tree, node.right)
        print(node.value)
        
postorder(tree, tree.root)
