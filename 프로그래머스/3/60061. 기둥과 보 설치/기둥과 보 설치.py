def build_col(x, y, n, curr_col, curr_row):
    # 기둥 설치
    if y == 0:  # 바닥 위
        return True
    elif curr_col[x][y - 1]:      # 다른 기둥 위
        return True
    elif curr_row[x][y]:          # 다른 보의 왼쪽 위
        return True
    elif curr_row[x - 1][y]:     # 다른 보의 오른쪽 위
        return True
    return False

def build_row(x, y, n, curr_col, curr_row):
    if x < n and curr_col[x][y - 1]:                  # 왼쪽 끝이 기둥 위
        return True
    elif x < n and curr_col[x + 1][y - 1]:            # 오른쪽 끝이 기둥 위
        return True
    elif 1 <= x < n - 1 and curr_row[x - 1][y] and curr_row[x + 1][y]:
        return True
    return False

def destroy(x, y, n, curr_col, curr_row):
    # 일단 없애고, 인접 기둥 / 보 규칙이 안 깨지는지 확인
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n and 0 <= ny <= n:
                if curr_col[nx][ny]:
                    if not build_col(nx, ny, n, curr_col, curr_row):
                        return False
                if curr_row[nx][ny]:
                    if not build_row(nx, ny, n, curr_col, curr_row):
                        return False
    return True

def solution(n, build_frame):
    curr_col = [[0] * (n + 1) for _ in range(n + 1)]
    curr_row = [[0] * (n + 1) for _ in range(n + 1)]
    # 0 -> 없음, 1 -> 있음
    
    for x, y, a, b in build_frame:
        if b == 1:          # 설치
            if a == 0:      # 기둥
                if build_col(x, y, n, curr_col, curr_row):
                    curr_col[x][y] = 1
            elif a == 1:    # 보
                if build_row(x, y, n, curr_col, curr_row):
                    curr_row[x][y] = 1
        elif b == 0:        # 철거
            if a == 0:
                curr_col[x][y] = 0
                if not destroy(x, y, n, curr_col, curr_row):
                    curr_col[x][y] = 1
            elif a == 1:
                curr_row[x][y] = 0
                if not destroy(x, y, n, curr_col, curr_row):
                    curr_row[x][y] = 1
    
    result = []
    for x in range(n + 1):
        for y in range(n + 1):
            if curr_col[x][y] == 1:
                result.append([x, y, 0])
            if curr_row[x][y] == 1:
                result.append([x, y, 1])
    result.sort()
    
    return result