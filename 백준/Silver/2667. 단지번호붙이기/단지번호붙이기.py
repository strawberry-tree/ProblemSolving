# DFS

# 그냥 코드는 너무 느리더라. 백준에선 아래 주석 해제하고 제출함.
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = []
visited = [[False] * N for _ in range(N)] # BFS의 방문여부
answer = [] # 단지별 집의 수

for _ in range(N):
    grid.append(list(map(int, input())))
    # 본 문제에선 input에 공백이 없음에 유의

def dfs(x, y):
    global houses
    # 2차원 배열 문제 -> 방향 벡터
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited[x][y] = True
    houses += 1

    for i in range(4):
        # 상하좌우로 한칸 이동할 때 새 좌표
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내에 있는지?
        if 0 <= nx < N and 0 <= ny < N:
            # 집이 있는 곳인지? 아직 방문하지 않은 곳인지?
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


# 모든 칸을 순회
# 아직 방문하지 않은 칸 -> 새로운 단지가 있다!
# 총 bfs 수행 횟수가, 단지의 개수
for x in range(N):
    for y in range(N):
        if grid[x][y] == 1 and not visited[x][y]:
            houses = 0
            dfs(x, y)
            answer.append(houses)

# 단지 수
print(len(answer))

# 단지별 집의 개수, 오름차순으로
answer.sort()
for a in answer:
    print(a)
