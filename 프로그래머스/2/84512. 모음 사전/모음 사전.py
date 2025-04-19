def dfs(word, target, index):
    # word: 현재 노드의 단어
    # target: 찾는 단어
    # index: 현재 노드의 인덱스
    if word == target:
        return index, True

    if len(word) == 5:
        return index, False

    for letter in "AEIOU":
        index, flag = dfs(word + letter, target, index + 1)
        if flag:
            return index, True

    return index, False

def solution(word):
    return dfs("", word, 0)[0]
