M = int(input())
dice = []
for _ in range(M):
    dice.append(list(map(int, input().split())))
magic = 1_000_000_007

# a^b 계산. 매번 r의 나머지로 나눠줌.
def square(a, b, r):
    if b == 0:
        return 1 % r
    
    half = square(a, b // 2, r) % r
    if b % 2 == 0:
        return half * half % r
    else:
        return half * half * a % r

def get_inverse(n):
    result = square(n, magic - 2, magic) % magic
    return result
        
total = 0
for n, s in dice:
    total = (total + get_inverse(n) * s) % magic
print(total)
            