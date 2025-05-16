import math

def check_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    for i in range(n // 2, 0, -1):
        if check_prime(i) and check_prime(n - i):
            print(i, n - i)
            break