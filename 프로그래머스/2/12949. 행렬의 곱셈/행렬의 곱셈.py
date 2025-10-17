def solution(arr1, arr2):
    M = len(arr1)       # 최종 행렬 행
    P = len(arr2)
    N = len(arr2[0])    # 최종 행렬 열
    answer = [[0] * N for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            for k in range(P):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer