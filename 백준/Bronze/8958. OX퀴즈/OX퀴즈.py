n = int(input())
for _ in range(n):
    total = 0
    point = 0
    case = input()
    for c in case:
        if c == "O":
            point += 1
            total += point
        else:
            point = 0
    print(total)