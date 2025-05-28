import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    result = bisect.bisect_right(A, target) - bisect.bisect_left(A, target)
    if result > 0:
        print(1)
    else:
        print(0)