a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)

for i in "0123456789":
    print(result.count(i))