def solution(keyinput, board):
    max_x = (board[0] - 1) // 2
    max_y = (board[1] - 1) // 2
    
    inputs = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    
    cx, cy = 0, 0
    for key in keyinput:
        dx, dy = inputs[key]
        nx, ny = cx + dx, cy + dy
        
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            cx, cy = nx, ny
    
    return [cx, cy]