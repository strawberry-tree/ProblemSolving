import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sums = [0]

for i in numbers:
    sums.append(sums[-1] + i)

for i in range(M):
    start, stop = map(int, input().split())
    print(sums[stop] - sums[start-1])