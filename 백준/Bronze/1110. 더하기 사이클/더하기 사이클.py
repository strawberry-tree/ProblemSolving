N = input()

def change_num(N):
    first_digit = N[-1]
    second_digit = str(sum(int(i) for i in N))[-1]
    result = first_digit + second_digit
    return result

count = 1
curr = change_num(N)

while int(curr) != int(N):
   curr = change_num(curr)
   count += 1
print(count)