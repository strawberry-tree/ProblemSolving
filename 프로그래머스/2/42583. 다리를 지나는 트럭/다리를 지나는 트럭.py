from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    bridge_queue = deque([-1] * bridge_length)
    time = 0
    current_weight = 0
    crossed_trucks = 0
    
    while crossed_trucks < len(truck_weights):
        time += 1
        
        # 기존 트럭들은 1칸씩 이동
        out = bridge_queue.popleft()
        if out != -1:
            current_weight -= out
            crossed_trucks += 1
        
        # 새로운 트럭이 들어갈 수 있으면 진입
        if truck_queue and (current_weight + truck_queue[0] <= weight):
            truck = truck_queue.popleft()
            current_weight += truck
            bridge_queue.append(truck)
        else:
            bridge_queue.append(-1)
    
    return time
        
        
        
        
        
            

            
        