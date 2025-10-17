from collections import Counter
def solution(want, number, discount):
    def check(dis_counter):
        for j in range(len(want)):
            if dis_counter[want[j]] != number[j]:
                return False
        return True
    answer = 0
    
    for i in range(len(discount) - 9):
        dis_counter = Counter(discount[i:i+10])
        if check(dis_counter):
            answer += 1

    return answer