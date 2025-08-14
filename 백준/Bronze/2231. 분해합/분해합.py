# N = 1000000이니까 brute force로 풀기

N = int(input())

def find_maker(N):
    for i in range(1, N + 1):
        # 자릿수 합
        digit_sum = sum(map(int, str(i)))
        if digit_sum + i == N:
            return i

    # 못 찾으면 0
    return 0

print(find_maker(N))