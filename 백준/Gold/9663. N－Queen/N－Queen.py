N = int(input())

cols = [False] * N              # 열 정보
diag_a = [False] * (2 * N - 1)  # / 대각선 정보
diag_b = [False] * (2 * N - 1)  # \ 대각선 정보

def place_row(i):
    if i >= N:
        return 1
    
    count = 0
    for j in range(N):
        if (not cols[j] and not diag_a[i + j] and not diag_b[i - j + N - 1]):
            cols[j] = diag_a[i + j] = diag_b[i - j + N - 1] = True
            count += place_row(i + 1)
            cols[j] = diag_a[i + j] = diag_b[i - j + N - 1] = False
    return count
    
print(place_row(0))