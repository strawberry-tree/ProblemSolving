def solution(want, number, discount):
    # 정현이가 원하는 상품 - 최대 10번 연산
    want_number = dict()
    for i in range(len(want)):
        want_number[want[i]] = number[i]
    
    # 딕셔너리에서 현재 할인상품 넣으면서 비교 - O(N)
    result = 0
    for i, name in enumerate(discount):
        if name in want_number:
            want_number[name] -= 1
        if i >= 10 and discount[i - 10] in want_number:
            want_number[discount[i - 10]] += 1
            
        # want_number의 모든 value가 0 이하일 때 - 최대 10번 연산
        if all(x <= 0 for x in want_number.values()):
            result += 1

    return result