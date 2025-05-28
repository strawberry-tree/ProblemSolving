N = int(input())
grid = []

for _ in range(N):
    grid.append(input())
    
# 영상이 한 숫자로만 이루어져 있는지
# 아니면 섞여 있는지
def check_num(N, x, y):
    first_num = grid[x][y]
    for i in range(N):
        for j in range(N):
            if grid[x + i][y + j] != first_num:
                return None
    return first_num

# 크기 N, x행 y열부터 시작
def compress(N, x, y):
    result = check_num(N, x, y)
    if result is not None:
        return result

    half = N // 2
    blockA = str(compress(half, x, y))
    blockB = str(compress(half, x, y + half))
    blockC = str(compress(half, x + half, y))
    blockD = str(compress(half, x + half, y + half))
    return f"({blockA}{blockB}{blockC}{blockD})"

print(compress(N, 0, 0))