def solution(record):
    user_dict = dict()
    talk_actions = [] # ("Enter" / "Leave", user_id)
    
    for r in record:
        r_list = r.split()
        
        if r_list[0] == "Enter":
            user_dict[r_list[1]] = r_list[2]
            talk_actions.append(("Enter", r_list[1]))
        elif r_list[0] == "Leave":
            talk_actions.append(("Leave", r_list[1]))
        elif r_list[0] == "Change":
            user_dict[r_list[1]] = r_list[2]
            
    answer = []
    for action, user_id in talk_actions:
        if action == "Enter":
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")
    
    return answer