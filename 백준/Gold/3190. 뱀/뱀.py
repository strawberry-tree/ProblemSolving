from collections import deque
import sys

input = sys.stdin.readline

N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수

# 배열의 값: 뱀이 마지막으로 해당 칸을 지난 시간
# 초기값은 -1
grid = [[-1] * N for _ in range(N)]
grid[0][0] = 0

# 사과의 위치
apples = set()         
for _ in range(K):
    a, b = map(int, input().split())
    apples.add((a - 1, b - 1))
    
L = int(input())    # 뱀의 방향변환 정보
queue = deque()

# 시간 및 명령
for _ in range(L):
    time, command = input().split()
    queue.append((int(time), command))
    
# 게임이 언제 끝나는지 반환
def gameplay():
    face = 0        # 우회전이면 +1, 좌회전이면 -1
    curr_time = 0   # 몇 초?
    head_x = 0      # 머리의 위치 - 몇행?
    head_y = 0      # 머리의 위치 - 몇열?
    length = 1      # 현재 뱀의 길이
    
    # 뱀이 이동하는 좌표를 반환
    def move():
        # 이동 방향 (순서대로 우 -> 하 -> 좌 -> 상)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        nx, ny = head_x + dx[face], head_y + dy[face]
        if nx < 0 or N <= nx or ny < 0 or N <= ny:
            return None    # 벽에 부딪힘 -> 게임 끝!
        if grid[nx][ny] >= curr_time - length:
            return None    # 뱀에 부딪힘 -> 게임 끝!
        # 해당 칸으로 이동
        grid[nx][ny] = curr_time
        return nx, ny
        
    while True:
        if not queue:
            set_time = float('inf')
        else:
            set_time, change = queue.popleft()
        
        # set_time 초 까지 움직임
        while curr_time < set_time:
            curr_time += 1
            move_result = move()
            if move_result is None:
                return curr_time
            head_x, head_y = move_result
            
            # 사과가 있는 경우
            if (head_x, head_y) in apples:
                apples.remove((head_x, head_y))
                length += 1
                    
        # 방향을 회전한다
        if change == "L":
            face -= 1
            if face < 0:
                face = 3 
        elif change == "D":
            face += 1
            if face >= 4:
                face = 0
                 
print(gameplay())
                
        
