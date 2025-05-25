N = int(input())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))
    
# 현재 종이 내 잘라진 하얀색 / 파란색 색종이의 개수 세기

# N: 한 변의 길이
# 맨 왼쪽 위 칸 -> x행 y열
def check(N, x, y):
    # 종이의 숫자 합
    total = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
           total += grid[i][j] 
    
    if total == 0:        # 하얀 종이
        return 1, 0
    elif total == N ** 2: # 파란 종이
        return 0, 1
    else:                 # 하얀색, 파란색이 섞임
        white, blue = 0, 0
        half = N // 2
        
        x_list = [x, x, x + half, x + half]
        y_list = [y, y + half, y, y + half]
        
        # 종이를 4등분
        # 4등분한 종이 내 하얀색 / 파란색 색종이 수 세기
        for i in range(4):
            cut = check(half, x_list[i], y_list[i])
            white += cut[0]
            blue += cut[1]
        
        return white, blue
    
result = check(N, 0, 0)
print(result[0])
print(result[1])