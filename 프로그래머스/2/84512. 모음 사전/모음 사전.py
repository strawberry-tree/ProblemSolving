def dfs(word, target, index):
    if word == target:
        return index, True
    
    if len(word) != 5:
        for letter in "AEIOU":
            index, flag = dfs(word + letter, target, index + 1)
            if flag:
                return index, flag
        
    return index, False
        
def solution(word):
    return dfs("", word, 0)[0]
