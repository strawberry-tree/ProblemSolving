# 입력 받기 및 빈칸 확인        
sudoku = [[0] * 9 for _ in range(9)]
spots = []

for i in range(9):
    input_list = list(map(int, input().split()))
    for j in range(9):
        num = input_list[j]
        sudoku[i][j] = num
        if num == 0:
            spots.append((i, j))
            
N = len(spots)

# x행 y열에 f 넣기
# 가능하면 True 불가능하면 False
def fill_spot(x, y, f):
    for k in range(9):
        if sudoku[x][k] == f:   # 같은 행
            return False
        if sudoku[k][y] == f:   # 같은 열
            return False
        
    bx = x // 3 * 3
    by = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[bx + i][by + j] == f:
                return False
    return True

# order번째 빈 칸 채우기
def fill_sudoku(order):
    if order >= N:
        return True
    
    # order번째 빈 칸의 x, y좌표
    x, y = spots[order]
    
    
    # 1부터 10까지 넣어보며 시도
    for f in range(1, 10):
        # 가로줄, 세로줄
        if fill_spot(x, y, f):
            sudoku[x][y] = f
            if fill_sudoku(order + 1):
                return True
            sudoku[x][y] = 0
            

# 스도쿠 채우기
fill_sudoku(0)

# 스도쿠 출력하기
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end=" ")
    print()