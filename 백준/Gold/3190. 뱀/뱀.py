from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수

# 사과의 위치
apples = set()         
for _ in range(K):
    a, b = map(int, input().split())
    apples.add((a - 1, b - 1))
    
L = int(input())    # 뱀의 방향변환 정보
comm_queue = deque() # 모든 방향변환 정보를 담은 큐

# 시간 및 명령
for _ in range(L):
    time, command = input().split()
    comm_queue.append((int(time), command))
    
# 게임이 언제 끝나는지 반환
def gameplay():
    curr_time = 0   # 지금 몇 초?
    head_x = 0      # 머리의 위치 - 몇행?
    head_y = 0      # 머리의 위치 - 몇열?
    
    # 현재 뱀이 존재하는 칸의 모든 좌표
    snake_queue = deque([(0, 0)])
    
    # 이동 방향 (순서대로 우 -> 하 -> 좌 -> 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    face = 0        # 우회전이면 +1, 좌회전이면 -1
        
    while True:
        curr_time += 1
        
        # 뱀 위치 이동
        nx, ny = head_x + dx[face], head_y + dy[face]
        if nx < 0 or N <= nx or ny < 0 or N <= ny:
            return curr_time    # 벽에 부딪힘 -> 게임 끝!
        if (nx, ny) in snake_queue:
            return curr_time    # 뱀에 부딪힘 -> 게임 끝!
        snake_queue.append((nx, ny))    # 머리의 위치를 큐에 추가
        head_x, head_y = nx, ny
        
        # 사과가 있는 경우
        if (head_x, head_y) in apples:
            apples.remove((head_x, head_y))
        else:
            snake_queue.popleft() # 꼬리의 위치를 큐에서 빼기
                    
        # 시간이 된 경우, 방향을 회전한다
        if comm_queue and comm_queue[0][0] == curr_time:
            command = comm_queue.popleft()[1]
            if command == "L":
                face = (face - 1) % 4
            else:
                face = (face + 1) % 4
                 
print(gameplay()) 
                
        
