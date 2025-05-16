T = int(input())
nums = []

for _ in range(T):
    nums.append(int(input()))
max_n = max(nums)

is_prime = [True] * (max_n + 1)     # 소수인 경우 True, 아니면 False
is_prime[1] = False                 # 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, max_n // 2 + 1):
    if not is_prime[i]:
        continue
    
    j = 2
    while i * j <= max_n:
        is_prime[i * j] = False
        j += 1

for n in nums:
    for i in range(n // 2, 0, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break