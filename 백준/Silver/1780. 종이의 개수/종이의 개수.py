import sys
input = sys.stdin.readline
N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

# NxN 크기이며 x행 y열로 시작하는 종이의 숫자 구성 확인
def check_num(N, x, y):
    first_num = grid[x][y]
    for i in range(N):
        for j in range(N):
            if grid[x+i][y+j] != first_num:
                return None
    return first_num
    
# NxN 크기이며 x행 y열로 시작하는 종이 자르기
def cut(N, x, y):
    count = {-1: 0, 0: 0, 1: 0} # 각각 몇 개?
    result = check_num(N, x, y)
    if result is not None:
        count[result] = 1
        return count

    x_list = [x, x + (N // 3), x + 2 * (N // 3)]
    y_list = [y, y + (N // 3), y + 2 * (N // 3)]
    for x in x_list:
        for y in y_list:
            block_result = cut(N // 3, x, y)
            for key in block_result:
                count[key] += block_result[key]
                
    return count

final_result = cut(N, 0, 0)
print(final_result[-1])
print(final_result[0])
print(final_result[1])