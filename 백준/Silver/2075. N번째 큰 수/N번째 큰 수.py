import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
curr_row = 0

for _ in range(N):
    for num in map(int, input().split()):
        heapq.heappush(heap, num)
    if len(heap) > N:
        for _ in range(N):
            heapq.heappop(heap)

print(heap[0])