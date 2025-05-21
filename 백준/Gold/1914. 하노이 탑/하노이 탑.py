def hanoi(n, start, end, sub):
    count = 0
    if n >= 2:
        count += hanoi(n - 1, start, sub, end)
    log.append((start, end))
    count += 1
    if n >= 2:
        count += hanoi(n - 1, sub, end, start)
    return count

N = int(input())
log = []

if N <= 20:
    print(hanoi(N, 1, 3, 2))
    for start, end in log:
        print(start, end)
else:
    print(2 ** N - 1)