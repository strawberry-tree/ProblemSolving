def solution(n, words):
    used_words = set()

    for idx, word in enumerate(words):
        # 이미 사용한 단어 OR 끝말잇기가 되지 않음
        if (word in used_words) or (1 <= idx and words[idx-1][-1] != word[0]):
            return [idx % n + 1, idx // n + 1]
        else:
            used_words.add(word)

    return [0, 0]