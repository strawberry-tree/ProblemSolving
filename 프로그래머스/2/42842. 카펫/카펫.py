import math
def solution(brown, yellow):
    area = brown + yellow
    for sero in range(3, int(math.sqrt(area)) + 1):
        if area % sero == 0:
            garo = area // sero
            if (garo - 2) * (sero - 2) == yellow:
                return [garo, sero]