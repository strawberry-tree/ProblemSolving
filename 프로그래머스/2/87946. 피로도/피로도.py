def enter(n, visited, k, dungeons):
    # n: 지금까지 들어간 던전 수
    answer = n
    
    # i: 들어갈 던전
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and i not in visited:
            visited.add(i)
            answer = max(answer, enter(n + 1, visited, k - dungeons[i][1], dungeons))
            visited.remove(i)
    
    return answer

def solution(k, dungeons):
    visited = set()
    return enter(0, visited, k, dungeons)
