import sys
input = sys.stdin.readline

n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)

for i in range(1, n + 1):
    stair = int(input())
 
    if i == 1:
        a[i] = stair
        b[i] = stair
    else:
        a[i] = b[i-1] + stair
        b[i] = max(a[i-2], b[i-2]) + stair

print(max(a[n], b[n]))