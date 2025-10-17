def solution(n):
    tiles = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i == 1:
            tiles[i] = 1
        elif i == 2:
            tiles[i] = 2
        else:
            tiles[i] = (tiles[i-1] + tiles[i-2]) % 1000000007
    return tiles[n]