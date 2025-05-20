def get_stars(n):
    if n == 3:
        return set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2,0), (2, 1),(2, 2)])
    
    n_div3 = n // 3
    before = get_stars(n_div3)
    result = set()
    dx = [0, 1, 2, 0, 2, 0, 1, 2]
    dy = [0, 0, 0, 1, 1, 2, 2, 2]
    
    for x, y in before:
        for i in range(8):
            nx = x + dx[i] * n_div3
            ny = y + dy[i] * n_div3
            result.add((nx, ny))
            
    return result

def draw_stars(n):
    array = [[False] * n for _ in range(n)]
    stars = get_stars(n)
    
    for i in range(n):
        for j in range(n):
            if (i, j) in stars:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
n = int(input())
draw_stars(n)