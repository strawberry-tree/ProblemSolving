length = int(input())
word = input()
answer = 0
buffer = []

# 한 번에 한 글자씩
for letter in word:
    if letter.isdigit():
        buffer.append(letter)
    else:
        if 1 <= len(buffer) <= 6:
            answer += int("".join(buffer))
        buffer = []

# 마지막에 남은 글자들 처리    
if 1 <= len(buffer) <= 6:
    answer += int("".join(buffer))

    
print(answer)