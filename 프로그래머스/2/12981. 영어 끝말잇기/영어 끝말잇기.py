def solution(n, words):
    used_words = set([words[0]])      # 이미 사용된 단어
    
    for i in range(1, len(words)):
        number = i % n + 1          # 몇 번째 사람?
        order = i // n + 1          # 몇 번째 차례?
        
        # 이미 사용한 단어가 아니면 탈락
        if words[i] in used_words:
            return [number, order]
        
        # 끝말잇기 조건 만족하지 않으면 탈락
        if words[i][0] != words[i - 1][-1]:
            return [number, order]
        
        # 이미 사용한 단어를 집합에 추가
        used_words.add(words[i])
        
    # 탈락자가 없어
    return [0, 0]