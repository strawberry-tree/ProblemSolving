from collections import Counter

def solution(participant, completion):
    par_set = Counter(participant)
    
    for c in completion:
        par_set[c] -= 1
        
    for key in par_set:
        if par_set[key] == 1:
            return key