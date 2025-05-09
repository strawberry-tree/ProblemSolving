from functools import cmp_to_key

def compare(x, y):
    a = int(x + y)
    b = int(y + x)
    
    return a - b


def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=cmp_to_key(compare), reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))