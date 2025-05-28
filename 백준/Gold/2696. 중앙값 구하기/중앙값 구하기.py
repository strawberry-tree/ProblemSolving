import heapq
T = int(input())

def print_mid(M, nums):
    max_heap = []
    min_heap = []
    mid_values = []
        
    for i in range(M):
        if i == 0 or nums[i] <= mid_value:
            heapq.heappush(max_heap, -nums[i])
        else:
            heapq.heappush(min_heap, nums[i])
        
        max_heap_len = (i + 2) // 2
        if len(max_heap) < max_heap_len:
            popped = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -popped)
        elif len(max_heap) > max_heap_len:
            popped = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, popped)
        
        mid_value = -max_heap[0]
        if i % 2 == 0:
            mid_values.append(mid_value)
            
    print(len(mid_values))
    for i in range(len(mid_values)):
        print(mid_values[i], end=" ")
        if i % 10 == 9 or i == len(mid_values) -1:
            print()            

for _ in range(T):
    M = int(input())
    nums = []
    while len(nums) < M:
        nums.extend(map(int, input().split()))
    print_mid(M, nums)