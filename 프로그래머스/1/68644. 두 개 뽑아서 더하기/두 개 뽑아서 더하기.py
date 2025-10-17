def solution(numbers):
    result_set = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result = numbers[i] + numbers[j]
            result_set.add(result)
            
    answer = list(result_set)
    answer.sort()
    return answer