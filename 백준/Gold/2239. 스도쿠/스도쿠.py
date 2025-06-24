import sys
sys.setrecursionlimit(10**9)

grid = []
for _ in range(9):
    grid.append(list(map(int, input())))
    
blanks = []

# x번째 행에 숫자 y의 존재 여부 -> TF
check_row = [[False] * 9 for _ in range(9)]

# x번째 열에 숫자 y의 존재 여부 -> TF
check_col = [[False] * 9 for _ in range(9)]

# x번째 3x3 정사각형에 숫자 y의 존재 여부 -> TF
check_box = [[False] * 9 for _ in range(9)]


for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            blanks.append((i, j))
        else:
            num = grid[i][j] - 1
            check_row[i][num] = True
            check_col[j][num] = True
            box_num = (i // 3) * 3 + (j // 3)
            check_box[box_num][num] = True
            

# idx번째 칸을 채운다
def fill(idx):
    if idx == len(blanks):
        # 모두 채운 경우
        return True
    
    i, j = blanks[idx]
    box_num = (i // 3) * 3 + (j // 3)
    for num in range(9):
        if not check_row[i][num]:
            if not check_col[j][num]:
                if not check_box[box_num][num]:
                    grid[i][j] = num + 1
                    check_row[i][num] = True
                    check_col[j][num] = True
                    check_box[box_num][num] = True
            
                    if fill(idx + 1):
                        return True
                    
                    grid[i][j] = 0
                    check_row[i][num] = False
                    check_col[j][num] = False
                    check_box[box_num][num] = False
            
fill(0)
for i in range(9):
    print(*grid[i], sep="")
    