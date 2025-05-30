import sys
input = sys.stdin.readline

N = int(input())
tree = dict()

for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)
    
# 전위 순회
def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])
    
# 중위 순회
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])
    
# 후위 순회
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")
        
preorder('A')
print()
inorder('A')
print()
postorder('A')