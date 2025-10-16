def square_possible(park, x, y, mat_side):
    for dx in range(mat_side):
        for dy in range(mat_side):
            if park[x + dx][y + dy] != "-1":
                return False
    return True
    
def check_len(park, mat_side):
    mat_x_len = len(park)
    mat_y_len = len(park[0])
    for x in range(mat_x_len - mat_side + 1):
        for y in range(mat_y_len - mat_side + 1):
            if square_possible(park, x, y, mat_side):
                return True
    return False
    
def solution(mats, park):
    answer = 0

    mats.sort(reverse = True)
    
    for mat_side in mats:
        if check_len(park, mat_side):
            return mat_side
    return -1
    
    
                            
    
    