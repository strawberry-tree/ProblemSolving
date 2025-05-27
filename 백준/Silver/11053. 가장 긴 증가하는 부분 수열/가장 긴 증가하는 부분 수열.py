N = int(input())
A = list(map(int, input().split())) # 수열 A

# 수열 A의 i번째 원소가 부분수열의 마지막 원소일 때,
# 해당 부분수열의 최대 길이는?
longest = []

for i in range(N):
    # 자신 이하의 값으로 끝나는 부분수열들 중
    # 최대 길이를 계산한다.
    prev = 0
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            prev = max(longest[j], prev)
    longest.append(prev + 1)
    
print(max(longest))