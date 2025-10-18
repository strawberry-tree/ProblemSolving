from functools import cmp_to_key

def compare(str1, str2):
    str1_first = int(str1 + str2)
    str2_first = int(str2 + str1)
    
    if str1_first > str2_first:
        return -1
    elif str1_first < str2_first:
        return 1
    return 0
        

def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key = cmp_to_key(compare))
    return str(int("".join(numbers)))