import sys
input = sys.stdin.readline

a = int(input())
b_str = input().strip()
result = 0

for i in range(3):
    mul = a * int(b_str[2 - i])
    print(mul)
    result += mul * (10 ** i)
print(result)