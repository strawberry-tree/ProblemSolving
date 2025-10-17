from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    q_goal = deque(goal)
    
    while (q1 or q2) and (q_goal):
        if q1 and q1[0] == q_goal[0]:
            q1.popleft()
            q_goal.popleft()
        elif q2 and q2[0] == q_goal[0]:
            q2.popleft()
            q_goal.popleft()
        else:
            return "No"
    
    if not q_goal:
        return "Yes"
    else:
        return "False"