def solution(people, limit):
    i = 0
    j = len(people) - 1
    answer = 0
    people.sort()
    
    while i <= j:
        answer += 1
        if i != j and people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
    
    return answer