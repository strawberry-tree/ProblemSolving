def add(numbers, target, idx, total):
    answer = 0
    
    if idx == len(numbers):
        if total == target:
            return 1
        else:
            return 0
    
    answer += add(numbers, target, idx + 1, total + numbers[idx])
    answer += add(numbers, target, idx + 1, total - numbers[idx])
    
    return answer

def solution(numbers, target):
    return add(numbers, target, 0, 0)