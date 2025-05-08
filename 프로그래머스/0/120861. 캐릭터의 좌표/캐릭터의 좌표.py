def solution(keyinput, board):
    dxy = {"left": [-1, 0], "up": [0, 1], "right": [1, 0], "down": [0, -1]}
    x_lim = board[0] // 2
    y_lim = board[1] // 2
    
    x, y = 0, 0
    for k in keyinput:
        dx, dy = dxy[k]
        nx, ny = x + dx, y + dy
        if -x_lim <= nx <= x_lim and -y_lim <= ny <= y_lim:
            x, y = nx, ny
            
    return [x, y]