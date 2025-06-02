import sys
input = sys.stdin.readline

def insert_node(tree, node):
    global root
    
    if root is None:    # 루트노드가 없을 때
        tree[node] = [None, None]
        root = node
    else:
        curr = root # 현재 노드
        while True:
            if node == curr:    # 동일 값은 추가 불가
                break
            if node < curr:     # 왼쪽으로
                if tree[curr][0] is None:
                    tree[curr][0] = node
                    tree[node] = [None, None]
                curr = tree[curr][0]
                
            if node > curr:     # 오른쪽으로
                if tree[curr][1] is None:
                    tree[curr][1] = node
                    tree[node] = [None, None]
                curr = tree[curr][1]
            
def postorder(tree, node):
    visited = set()
    stack = [node]
    
    while stack:
        curr = stack[-1]
        if tree[curr][0] and tree[curr][0] not in visited:
            stack.append(tree[curr][0])
        elif tree[curr][1] and tree[curr][1] not in visited:
            stack.append(tree[curr][1])
        else:
            stack.pop()
            visited.add(curr)
            print(curr)
    
tree = dict()
root = None     # 트리의 루트 노드

while True:
    try:
        node = int(input())
    except:
        break
    insert_node(tree, node)

postorder(tree, root)