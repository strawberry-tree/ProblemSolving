import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

# O(N)
for _ in range(N):
    num = int(input())
    count[num] += 1

# O(K)
for i in range(1, len(count)):
    for _ in range(count[i]):
        print(i)
