import sys
import heapq
input = sys.stdin.readline

min_heap = []
max_heap = []

N = int(input())
mid_value = -float('inf')

for i in range(N):
    num = int(input())
    
    
    if num >= mid_value: # 중앙값 이상일 시
        heapq.heappush(min_heap, num)
    
    
    else: # 중앙값 미만일 시
        # 최대 힙은 음수 값
        heapq.heappush(max_heap, -num)
        
    # 길이 구하기는 O(1)    
    if len(min_heap) > len(max_heap):
        popped = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -popped)
    elif len(min_heap) + 1 < len(max_heap):
        popped = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, popped)
    
    mid_value = -max_heap[0]
    print(mid_value)