import sys
R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * C for _ in range(R)]
alphabets = [False] * 26
visited[0][0] = True

def alph_id(letter):
    return ord(letter) - ord('A')

alphabets[alph_id(board[0][0])] = True

def dfs(x, y):
    answer = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny]:
                l_id = alph_id(board[nx][ny])
                if not alphabets[l_id]:
                    visited[nx][ny] = True
                    alphabets[l_id] = True
                    answer = max(answer, dfs(nx, ny))
                    visited[nx][ny] = False
                    alphabets[l_id] = False

    return answer + 1

print(dfs(0, 0))
    