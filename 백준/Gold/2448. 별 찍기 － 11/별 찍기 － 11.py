N = int(input())

def draw_star(N):
    if N == 3:
        return ["  *  ", " * * ", "*****"]
    else:
        before = draw_star(N // 2)
        result = []
        
        for line in before:
            result.append(" " * (N // 2) + line + " " * (N // 2))
            
        for line in before:
            result.append(line + " " + line)
        
        return result
    
for line in draw_star(N):
    print(line)