from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
queue = deque()

for _ in range(M):
    x, y, k = map(int, input().split())
    # x를 만드는 데 y가 k개 필요해요!
    graph[y].append((x, k))
    indegree[x] += 1
    
# 부품 key를 만드는데 기본 부품이 얼마나 필요해요?
# value: {기본부품1: a개, 기본부품2: b개} 형태
how_many = dict()

# 기본부품의 번호
base = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        base.append(i)
        
for b1 in base:
    how_many[b1] = dict()
    for b2 in base:
        if b1 == b2:
            how_many[b1][b2] = 1
        else:
            how_many[b1][b2] = 0
            
while queue:
    x = queue.popleft()            
    for y, count in graph[x]:
        indegree[y] -= 1
        
        if y not in how_many:
            how_many[y] = dict()
            for b in base:
                how_many[y][b] = 0

        for b in base:
            how_many[y][b] += how_many[x][b] * count
        
        if indegree[y] == 0:
            queue.append(y)

for key, value in how_many[N].items():
    print(key, value)