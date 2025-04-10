def solution(arr):
    answer = []
    
    # arr의 각 원소를 순회, O(N)
    for a in arr:
        if answer and answer[-1] == a:
            pass
        else:
            answer.append(a)
    
    return answer