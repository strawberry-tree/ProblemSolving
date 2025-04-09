def solution(arr, divisor):
    answer = list(filter(lambda x: x % divisor == 0, arr))
    if len(answer) < 1:
        return [-1]
    answer.sort()
    return answer