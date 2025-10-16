from collections import Counter

def solution(points, routes):
    N = len(points)     # 운송포인트 수
    X = len(routes)     # 로봇 수

    # 각 로봇별 이동데이터 저장
    move_data = [[] for _ in range(X)] 
    
    # 최단 거리로 이동
    def shortest_path(robot_id, start, end):
        sx, sy = points[start - 1]  # 로봇의 시작 좌표
        ex, ey = points[end - 1]    # 로봇의 도착 좌표
    
        
        # x축 이동
        if sx < ex:
            for dx in range(sx + 1, ex + 1):
                move_data[robot_id].append((dx, sy))
        elif sx > ex:
            for dx in range(sx - 1, ex - 1, -1):
                move_data[robot_id].append((dx, sy))
                
        # y축 이동
        if sy < ey:
            for dy in range(sy + 1, ey + 1):
                move_data[robot_id].append((ex, dy))
        elif sy > ey:
            for dy in range(sy - 1, ey - 1, -1):
                move_data[robot_id].append((ex, dy))
        
    # 각 로봇의 경로 확인
    for robot_id in range(X):
        sx, sy = points[routes[robot_id][0] - 1]
        move_data[robot_id].append((sx, sy))
        for i in range(len(routes[robot_id]) - 1):
            shortest_path(robot_id, routes[robot_id][i], routes[robot_id][i + 1])

    # 겹치는 경우 세기
    answer = 0
    max_time = max(len(robot) for robot in move_data)
    for t in range(max_time):
        pos_count = Counter()
        for robot_id in range(X):
            if t < len(move_data[robot_id]):
                pos_count[move_data[robot_id][t]] += 1
        
        crashes = 0
        
        for v in pos_count.values():
            if v > 1:
                crashes += 1
        answer += crashes
    
    return answer