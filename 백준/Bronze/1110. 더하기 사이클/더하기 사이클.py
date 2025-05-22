N = input()

def change_num(N):
    # 앞에서 구한 합의 맨 오른쪽 자리 수
    first_digit = N[-1]
    
    # 각 자리의 숫자를 더하고 맨 오른쪽 자리 수
    second_digit = str(sum(int(i) for i in N))[-1]
    
    # 이어붙이고, 반환
    result = first_digit + second_digit
    return result

curr = change_num(N)
count = 1

# 숫자가 동일할 때까지 반복
while int(curr) != int(N):
   curr = change_num(curr)
   count += 1

print(count)