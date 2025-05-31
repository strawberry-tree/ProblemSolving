import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost
print(answer)