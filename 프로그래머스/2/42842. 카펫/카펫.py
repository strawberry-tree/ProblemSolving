import math

def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i != 0:
            continue
        height = i + 2
        width = (yellow // i) + 2
        if (width * height) == (brown + yellow):
            return [width, height]