n = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
    if num != 1:
        for div in range(2, num - 1):
            if num % div == 0:
                break
        else:
            result += 1

print(result)
