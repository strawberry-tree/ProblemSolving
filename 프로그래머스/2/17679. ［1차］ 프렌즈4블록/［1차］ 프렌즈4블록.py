def solution(m, n, board):
    def check_square(x, y, col_board):
        blocks = set()
        for i in range(2):
            for j in range(2):
                if 0 <= x + i < len(col_board) and 0 <= y + j < len(col_board[x + i]):
                    blocks.add(col_board[x + i][y + j])
                else:
                    return False
        
        return len(blocks) == 1
    
    # 행 M개 열 N개
    # 각 열을 2차원 리스트로 만듦
    col_board = []
    for y in range(n):
        column = []
        for x in range(m - 1, -1, -1):
            column.append(board[x][y])
        col_board.append(column)
    
    result = 0                                      # 지워지는 블록의 수
    
    while True:
        destroy = set()                             # (x행, y열) 저장
        
        # 모든 칸 확인하며 2x2로 묶인 블록 없애기
        for x in range(n - 1):
            for y in range(m - 1):
                # 모든 칸이 동일하면 없앨 수 있음
                if check_square(x, y, col_board):
                    for i in range(2):
                        for j in range(2):
                            destroy.add((x + i, y + j))
        
        if len(destroy) == 0:
            break
        else:
            result += len(destroy)
        
        # destroy에 포함된 칸 지우기
        new_board = [[] for _ in range(n)]
        for x in range(n):
            for y in range(len(col_board[x])):
                if (x, y) not in destroy:
                    new_board[x].append(col_board[x][y])
                    
        col_board = new_board
    return result