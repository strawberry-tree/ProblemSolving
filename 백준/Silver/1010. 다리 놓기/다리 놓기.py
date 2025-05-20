def check_combs(N, M):
    # M개 중 N개를 고르는 조합
    a = 1
    for i in range(M, M-N, -1):
        a *= i
    b = 1
    for j in range(2, N + 1):
        b *= j
    return a // b

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(check_combs(N, M))
