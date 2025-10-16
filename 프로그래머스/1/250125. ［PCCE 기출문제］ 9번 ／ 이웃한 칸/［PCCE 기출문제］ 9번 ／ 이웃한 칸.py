def solution(board, h, w):
    board_len = len(board)
    color = board[h][w]
    count = 0
    dh = [-1, 0, 1, 0]
    dw = [0, -1, 0, 1]
    
    for i in range(4):
        if 0 <= h + dh[i] < board_len and 0 <= w + dw[i] < board_len:
            if board[h + dh[i]][w + dw[i]] == color:
                count += 1
    return count