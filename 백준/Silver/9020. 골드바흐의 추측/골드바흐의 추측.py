import math

T = int(input())
nums = []

for _ in range(T):
    nums.append(int(input()))
max_n = max(nums)

# 에라토스테네스의 체
# 2부터 N까지 숫자 나열
is_prime = [True] * (max_n + 1)     # 소수인 경우 True, 아니면 False
is_prime[1] = False                 # 1은 소수가 아님

# sqrt(N)까지 아래 과정을 반복
for i in range(2, int(math.sqrt(max_n)) + 1):
    # 남은 숫자 중 가장 작은 숫자 -> i
    if is_prime[i]:
        # i의 배수를 모두 지움 (i * i 이전의 배수는 이미 지워졌음에 유의)
        for j in range(i * i, max_n + 1, i):
            is_prime[j] = False

for n in nums:
    for i in range(n // 2, 0, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break
            