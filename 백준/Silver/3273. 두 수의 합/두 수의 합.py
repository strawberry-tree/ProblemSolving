N = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

# [1, 2, 3, 5, 7, 9, 10, 11, 12]
i = 0
j = len(nums) - 1
count = 0

while i < j:
    result = nums[i] + nums[j]
    if result == x:
        count += 1
        i += 1
    elif result < x:
        i += 1
    else:
        j -= 1
        
print(count)