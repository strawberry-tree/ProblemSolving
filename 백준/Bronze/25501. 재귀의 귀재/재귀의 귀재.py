def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0 
    else:
        return recursion(s, l + 1, r - 1)
    
T = int(input())
s_list = []

for _ in range(T):
    s_list.append(input())
    
for t in range(T):
    count = 0
    s = s_list[t]
    print(recursion(s, 0, len(s)-1), count)