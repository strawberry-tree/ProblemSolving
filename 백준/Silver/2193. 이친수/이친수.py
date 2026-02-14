N = int(input())
fib = [0] * (N + 1)

for i in range(N + 1):
    if i == 0:
        fib[i] = 0
    elif i == 1:
        fib[i] = 1
    else:
        fib[i] = fib[i-1] + fib[i-2]
print(fib[N])