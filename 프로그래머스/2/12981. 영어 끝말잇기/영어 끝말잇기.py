def solution(n, words):
    used_words = set()
    
    for i in range(len(words)):
        word = words[i]
        
        if word in used_words:
            return [i % n + 1, i // n + 1]
        elif i >= 1 and words[i][0] != words[i-1][-1]:
            return [i % n + 1, i // n + 1]
        used_words.add(word)
            
    return [0, 0]