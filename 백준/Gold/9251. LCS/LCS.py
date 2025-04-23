str1 = input()
str2 = input()
N = len(str1)
M = len(str2)

# memo[i][j]: str1[0: i], str2[0: j]의 LCS 길이
memo = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 두 문자열의 마지막 문자가 동일
        if str1[i - 1] == str2[j - 1]:
            # 두 마지막 문자를 제외한 LCS 길이에 1 더함
            memo[i][j] = memo[i - 1][j - 1] + 1

        # 두 문자열의 마지막 문자가 동일하지 않음
        else:
            # 각 마지막 문자를 제외했을 때 LCS 길이 확인 후 최댓값
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[N][M])