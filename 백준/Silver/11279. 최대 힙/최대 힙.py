import heapq
import sys 

input = sys.stdin.readline
maxheap = []

N = int(input())
for _ in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(maxheap, -x)
    else:
        if not maxheap:
            print(0)
        else:
            print(-heapq.heappop(maxheap))