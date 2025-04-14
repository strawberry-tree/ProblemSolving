def solution(n,a,b):
    div = 2
    i = 1
    
    while True:
        if (a - 1) // div == (b - 1) // div:
            return i
        div *= 2
        i += 1