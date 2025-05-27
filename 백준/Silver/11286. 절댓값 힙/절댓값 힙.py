import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
queue = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, (abs(x), x))