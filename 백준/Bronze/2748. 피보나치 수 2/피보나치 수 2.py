N = int(input())
memo = [None] * (N + 1)
memo[0] = 0
memo[1] = 1

def fibo(x):
    if memo[x] is not None:
        return memo[x]
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]

print(fibo(N))