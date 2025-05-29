import bisect

N = int(input())
A = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
A.sort()

for t in targets:
    count = bisect.bisect_right(A, t) - bisect.bisect_left(A, t)
    if count > 0:
        print(1)
    else:
        print(0)