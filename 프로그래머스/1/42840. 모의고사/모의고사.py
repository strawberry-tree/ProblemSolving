def solution(answers):
    # 삼인방의 점수 배열
    points = [0, 0, 0]
    
    # 삼인방이 찍는 방식
    a_check = [1, 2, 3, 4, 5]
    b_check = [2, 1, 2, 3, 2, 4, 2, 5]
    c_check = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 문제를 순회하며 채점, O(N)
    for idx, answer in enumerate(answers):
        if answer == a_check[idx % len(a_check)]:
            points[0] += 1
        if answer == b_check[idx % len(b_check)]:
            points[1] += 1
        if answer == c_check[idx % len(c_check)]:
            points[2] += 1
        
    # 가장 많은 문제 수를 맞힌 사람을 result 배열에 추가
    result = []
    top_score = max(points)
    for idx in range(3):
        if points[idx] == top_score:
            result.append(idx + 1)
            
    return result