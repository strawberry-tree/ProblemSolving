def solution(participant, completion):
    # 사전으로 만들기 - O(N)
    p_dict = dict()
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1
    
    # 완주한 사람 확인 - O(N)
    for p in completion:
        p_dict[p] -= 1
        
    # 완주 못 한 사람 찾기 - O(N)
    for key, value in p_dict.items():
        if value != 0:
            return key