def draw_stars(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    n_div3 = n // 3
    before = draw_stars(n_div3)
    result = []
    
    for line in before:
        result.append(line * 3)
    
    for line in before:
        result.append(line + " " * n_div3 + line)
        
    for line in before:
        result.append(line * 3)
    return result
    
n = int(input())
stars = draw_stars(n)

for line in stars:
    print(line)