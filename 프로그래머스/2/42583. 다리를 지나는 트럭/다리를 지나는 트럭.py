from collections import deque

# 최종 시간복잡도: O(N)
def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge_queue = deque([0] * bridge_length)
    # 각 칸은 해당 칸에 위치한 차의 무게. 0은 차가 없는 칸, 무게도 0
    time = 0
    current_weight = 0
    
    # truck_weights의 길이를 N으로 둘 때 O(N)
    while truck_queue or current_weight > 0:
        time += 1
        
        # popleft() 하고 append() 함으로써 모든 트럭이 한 칸씩 전진
        out = bridge_queue.popleft()
        current_weight -= out
        
        if truck_queue and (current_weight + truck_queue[0] <= weight):
            # 새로운 트럭이 들어갈 수 있으면 진입
            truck = truck_queue.popleft()
            current_weight += truck
            bridge_queue.append(truck)
        
        else:
            # 들어갈 수 없으면 0으로 채움
            bridge_queue.append(0)
    
    return time        
