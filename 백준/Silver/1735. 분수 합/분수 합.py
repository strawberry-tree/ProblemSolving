import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

B = math.lcm(B1, B2)
A1_mul = B // B1
A2_mul = B // B2
A = A1_mul * A1 + A2_mul * A2

div = math.gcd(A, B)
A = A // div
B = B // div

print(A, B)