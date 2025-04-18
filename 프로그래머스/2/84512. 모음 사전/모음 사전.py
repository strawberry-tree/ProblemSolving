def solution(word):
    index = 0
    found = False
    
    def dfs(current, target):
        nonlocal index, found
    
        if found:
            return

        if current == target:
            found = True
            return

        if len(current) != 5:
            for letter in "AEIOU":
                index += 1
                dfs(current + letter, target)
                if found:
                    return

    
    dfs("", word)
    return index
