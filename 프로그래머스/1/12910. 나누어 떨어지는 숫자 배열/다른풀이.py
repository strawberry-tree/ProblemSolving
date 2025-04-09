# list comprehension 사용

def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if len(answer) < 1:
        return [-1]
    answer.sort()
    return answer
