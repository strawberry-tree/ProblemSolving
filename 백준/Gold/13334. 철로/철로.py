import sys
import heapq

input = sys.stdin.readline
n = int(input())
in_heap = []                # 각 선분의 시작점 좌표
out_heap = []               # 각 선분의 종료점 좌표

for _ in range(n):
    h, o = map(int, input().split())
    # (종료점 좌표, 시작점 좌표)
    heapq.heappush(out_heap, (max(h, o), min(h, o)))

d = int(input())   # 철근의 거리

# 현재 철근 집, 사무실이 포함되는 사람들
count_a = 0

# 철근 좌측에 집, 사무실이 있는 사람들
count_b = 0

# 철근에 포함되는 사람들의 최대 수
answer = 0

while out_heap:
    endpoint = out_heap[0][0]
    while out_heap and out_heap[0][0] == endpoint:
        x = heapq.heappop(out_heap)[1]
        heapq.heappush(in_heap, x)
        count_a += 1

    startpoint = endpoint - d  # 철근의 시작점
       
    while in_heap and in_heap[0] < startpoint:
        heapq.heappop(in_heap)
        count_b += 1

    answer = max(answer, count_a - count_b)
    
print(answer)