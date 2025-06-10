# 사실 마지막 주유소의 가격은 알 필요도 없긴 함

N = int(input())
roads = list(map(int, input().split()))
gas = list(map(int, input().split()))[:-1]

curr_gas = gas[0] 
curr_road = roads[0]
total = 0

for i in range(1, N - 1):
    if curr_gas >= gas[i]:
        total += curr_road * curr_gas
        curr_gas = gas[i]
        curr_road = roads[i]        
    else:
        curr_road += roads[i]
        
total += curr_road * curr_gas
print(total)
    