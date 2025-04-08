from itertools import combinations 

def solution(numbers):
    # 중복을 허용하지 않음 - 집합
    answer = set()
    
    # 두 개의 수를 뽑아 수 더하기
    for (a, b) in combinations(numbers, 2):
        answer.add(a + b)
    
    # 집합을 리스트로 변환 후, 오름차순으로 정렬
    answer = list(answer)
    answer.sort()
    return answer