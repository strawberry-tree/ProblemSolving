import math

T = int(input())
nums = []

for _ in range(T):
    nums.append(int(input()))
    
max_n = max(nums)

# 에라토스테네스의 체
is_prime = [True] * (max_n + 1)
is_prime[0] = False
is_prime[1] = False



for i in range(2, int(math.sqrt(max_n)) + 1):
    for num in range(i * i, max_n + 1, i):
        is_prime[num] = False


# 골드바흐 파티션 함수
def get_gp(n):
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            return i, n - i

# 출력하기
for n in nums:
    a, b = get_gp(n)
    print(a, b)