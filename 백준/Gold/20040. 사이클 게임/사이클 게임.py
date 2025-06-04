import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))
    
parent = [i for i in range(N)]
    
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a == b:
        return True
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a
        
    return False

for i, (a, b) in enumerate(edges):
    if union(parent, a, b):
        print(i + 1)
        break
else:
    print(0)
        