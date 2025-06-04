import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a == b:
        return
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(M):
    calc, a, b = map(int, input().split())
    
    if calc == 0:
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
            