import math

# 입력
cases = []

while True:
    n = int(input())
    if n == 0:
        break
    cases.append(n)

max_n = 2 * max(cases)

# 에라토스테네스의 체
is_prime = [True] * (max_n + 1)
is_prime[1] = False

for i in range(2, int(math.sqrt(max_n)) + 1):
    for j in range(i * i, max_n + 1, i):
        is_prime[j] = False

# 소수 개수 출력
for c in cases:
    print(sum(is_prime[c + 1: 2*c + 1]))