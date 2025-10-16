from collections import deque

def solution(bandage, health, attacks):
    cur_health = health     # 현재 체력
    time = 1                # 소요 시간
    consecutive_heal = 0    # 연속 힐링
    attacks_queue = deque(attacks)
    
    # 1초당 하는 일들 정리
    while True:
        # 공격을 받음
        if attacks_queue and attacks_queue[0][0] == time:
            cur_health -= attacks_queue[0][1]
            consecutive_heal = 0
            attacks_queue.popleft()
        
        # 공격받지 않음 = 붕대감기
        else:
            cur_health = min(cur_health + bandage[1], health)
            consecutive_heal += 1
            
            if consecutive_heal >= bandage[0]:
                cur_health = min(cur_health + bandage[2], health)
                consecutive_heal = 0
        
        # 죽은 경우
        if cur_health <= 0:
            return -1
        
        # 마지막 공격이 끝난 경우
        if len(attacks_queue) <= 0:
            return cur_health
        
        time += 1