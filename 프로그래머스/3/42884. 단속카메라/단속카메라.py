def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[1])
    i = 0
    camera_loc = routes[0][1]
    
    for r in routes[1:]:
        if r[0] > camera_loc:
            answer += 1
            camera_loc = r[1]
    answer += 1
                
    return answer