def mul(A, B, C):
    if B == 0:
        return 1
    else:
        if B % 2 == 0:
            return mul(A, B // 2, C) ** 2 % C
        else:
            return mul(A, B // 2, C) ** 2 * A % C
        
A, B, C = map(int, input().split())
print(mul(A, B, C))