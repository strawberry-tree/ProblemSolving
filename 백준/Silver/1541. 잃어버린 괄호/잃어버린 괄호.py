plus_list = list(input().split("-"))
minus_list = []

for p in plus_list:
    minus_list.append(sum(map(int, p.split("+"))))
    
answer = minus_list[0]
for i in range(1, len(minus_list)):
    answer -= minus_list[i]
print(answer)