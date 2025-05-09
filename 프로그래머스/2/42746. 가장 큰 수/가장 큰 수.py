from functools import cmp_to_key

def compare(x, y):
    a = x + y
    b = y + x
    
    if a < b:       # y + x가 더 큰 경우
        return -1   # x가 앞 순서
    elif b < a:     # x + y가 더 큰 경우
        return 1    # y가 앞 순서
    else:
        return 0    # 동일 시 순서를 바꾸지 않음


def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=cmp_to_key(compare), reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))