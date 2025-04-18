def enter(i, n, results, visited, k, dungeons):
    # i: 지금 들어간 던전, n: 탐험한 던전 수
    k -= dungeons[i][1]
    visited.add(i)
    
    for next_i in range(len(dungeons)):
        if k >= dungeons[next_i][0] and next_i not in visited:
            enter(next_i, n + 1, results, visited, k, dungeons)
    
    visited.remove(i)
    results.append(n)

def solution(k, dungeons):
    results = [0]
    visited = set()
    for first_i in range(len(dungeons)):
        if k >= dungeons[first_i][0]:
            enter(first_i, 1, results, visited, k, dungeons)
    
    return max(results)