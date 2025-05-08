def changebase(ten):
    result = []
    while ten:
        ten, r = divmod(ten, 2)
        result.append(str(r))
    result.reverse()
    return "".join(result)
        
def solution(s):
    count = 0
    removed = 0
    
    while s != "1":
        zeros = 0
        for digit in s:
            if digit == "0":
                zeros += 1
        removed += zeros
        s = changebase(len(s) - zeros)
        count += 1
    return [count, removed]