from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)
time = [0] * (N + 1)

for _ in range(M):
    start, end, edge = map(int, input().split())
    graph[start].append((end, edge))
    rev_graph[end].append((start, edge))
    indegree[end] += 1

begin, finish = map(int, input().split())    

def top_sort():
    queue = deque([begin])
            
    while queue:
        curr = queue.popleft()
        for adj, edge in graph[curr]:
            indegree[adj] -= 1
            newtime = time[curr] + edge
            if newtime > time[adj]:
                time[adj] = newtime
            if indegree[adj] == 0:
                queue.append(adj)



def bfs(finish):
    queue = deque([finish])
    edges = set()

    while queue:
        x = queue.popleft()
        for y, cost in rev_graph[x]:
            if time[y] + cost == time[x] and (y, x) not in edges:
                queue.append(y)
                edges.add((y, x))
                
    return(len(edges))

     
top_sort()
print(time[finish])
print(bfs(finish))