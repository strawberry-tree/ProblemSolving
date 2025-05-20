import sys
sys.setrecursionlimit(10**6)

def safe_areas(height):
    # grid는 각 칸의 높이 정보를, height는 물의 높이를 담은 변수 
    # 물에 빠진 칸은 True, 빠지지 않은 칸은 False
    checked = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] <= height:  # 물에 빠진 칸
                checked[i][j] = True
    
    # 인접한 물이 차지 않은 칸을 모두 방문 처리
    def check_spot(x, y, checked):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        checked[x][y] = True					# 지금 칸은 True로 처리
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]		# 상하좌우 인접 칸 확인
            if 0 <= nx < N and 0 <= ny < N:		# 범위를 안 벗어나는지?
                if not checked[nx][ny]:			# 값이 False인지?
                    check_spot(nx, ny, checked) # 재귀 호출
                    
    count = 0 # 총 안전 영역의 수

    # 각 칸을 순회
    # 물에 빠지지 않은 칸인 경우, count에 1을 더하고
    # check_spot() 사용해 인접 칸을 모두 True 처리
    for i in range(N):
        for j in range(N):
            if checked[i][j] == False:
                count += 1
                check_spot(i, j, checked)
    
    return count

# 입력 받기           
N = int(input())
grid = [[] for _ in range(N)]
min_height = 100
max_height = 1

for i in range(N):
    for val in list(map(int, input().split())):
        grid[i].append(val)
        min_height = min(min_height, val)
        max_height = max(max_height, val)

answer = 0

# 각 높이를 대상으로, 안전 영역의 수를 계산
for height in range(min_height - 1, max_height + 1):
    answer = max(answer, safe_areas(height))
                
print(answer)
    