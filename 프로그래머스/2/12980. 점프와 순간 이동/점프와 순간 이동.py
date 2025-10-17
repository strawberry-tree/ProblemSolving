def solution(n):
    ans = bin(n)[2:].count("1")
    return ans