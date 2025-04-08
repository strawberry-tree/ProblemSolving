def move(x, y, d):
    if d == "L":
        return (x - 1, y)
    elif d == "R":
        return (x + 1, y)
    elif d == "U":
        return (x, y + 1)
    elif d == "D":
        return (x, y - 1)

def solution(dirs):
    x, y = 0, 0
    answer = 0
    paths = [] # 좌표 tuple 2개로 구성된 set로 구성된 list...? 
    
    # 이동
    for d in dirs:
        nx, ny = move(x, y, d)
        
        # 이동 가능할 때
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            
            # 이미 간 길이 아니면, 이동한 길에 추가
            road = {(x, y), (nx, ny)}
            if road not in paths:
                paths.append(road)
            
            # 이동
            x, y = nx, ny

    return len(paths)