from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
# 0, ..., N-1 중에 M개 선택 (M = 1, 2, ... N)
for M in range(1, N + 1):
    for comb in combinations(range(N), M):
        total = 0
        for idx in comb:
            total += nums[idx]
        if total == S:
            count += 1
print(count)


# # 부분수열의 길이
# for i in range(1, N):
#     # 부분수열의 첫 인덱스
#     for j in range(N - i):
#         length = sum(nums[j:j+i])
#         if length == S:
#             count += 1
        
# print(count)
