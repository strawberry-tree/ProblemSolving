from collections import Counter

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))    
nums.sort()

# 산술평균
print(int(round(sum(nums) / N, 0)))

# 중앙값
print(nums[(N - 1) // 2])
    
# 최빈값
counter = Counter(nums).most_common()
freq = []
freq_count = counter[0][1]

for num, count in counter:
    if freq_count == count:
        freq.append(num)
    else:
        break

if len(freq) <= 1:
    print(freq[0])
else:
    print(freq[1])


# 범위
print(nums[-1] - nums[0])