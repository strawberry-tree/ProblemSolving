from math import factorial
N, M, K = map(int, input().split())
curr = 1
result = []

# 총 N + M 자리수
while N > 0 or M > 0:
    
    if M <= 0:
        result.append("a")
        N -= 1
    elif N <= 0:
        result.append("z") 
        curr += a_rest_num
        M -= 1

    else:
        # a 사용 시 나머지 경우의 수
        a_rest_num = int(factorial(N - 1 + M) / (factorial(N - 1) * factorial(M)))

        if curr + a_rest_num > K:
            N -= 1
            result.append("a")
        else:
            M -= 1
            curr += a_rest_num
            result.append("z")
            
if curr < K:
    print(-1)
else:
    print("".join(result))