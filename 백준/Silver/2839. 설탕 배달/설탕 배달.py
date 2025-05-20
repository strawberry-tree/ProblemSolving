N = int(input())
three_count = 0

for three_count in range(0, N // 3 + 1):
    # 최대한 5킬로그램을 많게
    # 즉 3킬로그램을 적게
    three_total = 3 * three_count
    five_total = N - three_total
    if five_total % 5 == 0:
        five_count = five_total // 5   
        print(three_count + five_count)
        break
    
else:
    print(-1)