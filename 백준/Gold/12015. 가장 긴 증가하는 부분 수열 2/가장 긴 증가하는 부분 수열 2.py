import bisect

N = int(input())
A = list(map(int, input().split())) # 수열 A

# tails[i]: 길이가 i인 수열의 끝값
tails = [0]

for i in range(N):
    if tails[-1] < A[i]:
        tails.append(A[i])
    else:
        loc = bisect.bisect_left(tails, A[i])
        tails[loc] = A[i]

# 지금까지 만든 부분수열 중 최대 길이
print(len(tails) - 1)