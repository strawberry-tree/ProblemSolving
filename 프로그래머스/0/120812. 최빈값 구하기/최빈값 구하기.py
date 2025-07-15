from collections import Counter

def solution(array):
    num_counts = Counter(array).most_common(2)
    
    # array가 숫자 1개로만 구성됐을 때 or 최빈값이 1개일 때
    if len(num_counts) == 1 or num_counts[0][1] != num_counts[1][1]:
        return num_counts[0][0]
    else:
        return -1