import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
stars = []
for _ in range(n):
    stars.append(tuple(map(float, input().split())))

def calc_dist(i, j):
    x1, y1 = stars[i]
    x2, y2 = stars[j]
    
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

lines = []

for i in range(n):
    for j in range(i + 1, n):
        if i != j:
            lines.append((calc_dist(i, j), i, j))
            
lines.sort()
parent = [i for i in range(n)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False
    elif a > b:
        parent[a] = b
    else:
        parent[b] = a
    return True

answer = 0

for cost, a, b in lines:
    if union(parent, a, b):
        answer += cost
        
print(answer)     