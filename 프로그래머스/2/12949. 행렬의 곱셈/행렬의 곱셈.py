def solution(arr1, arr2):
    # (A x B) 행렬과 (B x C) 행렬의 곱은 (A X C)
    n_rows = len(arr1)
    n_mid = len(arr2)
    n_cols = len(arr2[0])
    answer = [[0] * n_cols for _ in range(n_rows)]
    
    # 각 행과 각 열을 for문으로 불러옴
    for i in range(n_rows):
        for j in range(n_cols):
            result = 0            
            # 불러온 행, 열의 각 성분을 곱한 뒤 더함
            for k in range(n_mid):
                result += arr1[i][k] * arr2[k][j]
            answer[i][j] = result

    return answer