N = int(input())

# 1이 될 때까지 나눗셈
while N > 1:
    i = 2
    while True:
        # i로 나눠 떨어지면, i를 출력하고 N을 i로 나눔
        if N % i == 0:
            print(i)
            N = N // i
            break
        i += 1