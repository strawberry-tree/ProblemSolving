from collections import deque
import math

N = int(input())
visited = [False] * (N + 1)
queue = deque([(0, 0)])
squares = list(i * i for i in range(1, int(math.sqrt(N) + 1)))

def bfs():
    while queue:
        curr, dist = queue.popleft()
        if curr == N:
            return dist

        for sq in squares:
            adj = curr + sq
            if adj > N:
                break
            if not visited[adj]:
                queue.append((adj, dist + 1))
                visited[adj] = True
     
print(bfs())