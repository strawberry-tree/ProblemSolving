import sys
import heapq

input = sys.stdin.readline
n = int(input())

lines = []               # 각 선분의 좌표
in_heap = []             # 각 선분의 시작점을 저장할 힙

for _ in range(n):
    h, o = map(int, input().split())
    # (종료점 좌표, 시작점 좌표)
    lines.append((max(h, o), min(h, o)))

lines.sort()

d = int(input())   # 철근의 거리

# 철근 좌측에 집, 사무실이 있는 사람들
count = 0

# 철근에 포함되는 사람들의 최대 수
answer = 0

for end, start in lines:
    bridge_end = end
    heapq.heappush(in_heap, start)
    bridge_start = bridge_end - d  # 철근의 시작점
       
    while in_heap and in_heap[0] < bridge_start:
        heapq.heappop(in_heap)
        count += 1

    answer = max(answer, len(in_heap))
    
print(answer)