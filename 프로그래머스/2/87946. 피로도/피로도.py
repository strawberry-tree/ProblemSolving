# unvisited에 있는애들 방문가능, 현재체력 k, 현재방문 던전수 num
def visit(unvisited, k, num, dungeons, results):
    
    for j in unvisited:
        entry = dungeons[j][0]
        minus = dungeons[j][1]
        
        # 입장이 가능한 경우
        if entry <= k:
            unvisited.remove(j)
            visit(unvisited, k - minus, num + 1, dungeons, results)
            unvisited.add(j)
            
    # 지금까지 방문한 던전수
    results.append(num)

def solution(k, dungeons):
    unvisited = set(i for i in range(len(dungeons)))
    results = []
    visit(unvisited, k, 0, dungeons, results)
    return max(results)
    