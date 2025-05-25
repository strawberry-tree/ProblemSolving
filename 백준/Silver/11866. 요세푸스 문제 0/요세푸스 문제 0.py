n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
answer = []

while people:
    out = (k - 1) % len(people)
    answer.append(people[out])
    people = people[out + 1:] + people[:out] 

print("<", end="")
print(*answer, sep=', ', end="")
print(">")
