def hanoi(n, start, end):
    result = 1
    
    if n > 1:
        result += hanoi(n - 1, start, 6 - start - end)
    log.append((start, end))
    if n > 1:
        result += hanoi(n - 1, 6 - start - end, end)
        
    return result
        
n = int(input())
log = []
print(hanoi(n, 1, 3))
for s, e in log:
    print(s, e)