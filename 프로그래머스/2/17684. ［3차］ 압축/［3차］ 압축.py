def solution(msg):
    result = []
    
    # 사전 만들기
    lzw = dict()
    for i in range(26):
        lzw[chr(ord('A') + i)] = i + 1
    
    # 사전에 없을 때까지 윈도우 확장
    start = 0
    end = 1
    
    # 시간복잡도 O(N)
    while end < len(msg):
        if msg[start:end + 1] in lzw:
            end += 1
        else:
            result.append(lzw[msg[start:end]])
            lzw[msg[start:end + 1]] = len(lzw) + 1
            start = end
            end = start + 1
    
    if msg[start:end] in lzw:
        result.append(lzw[msg[start:end]])
            
    return result