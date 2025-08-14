X = input()         # 입력 정수

if X.startswith("0x"):
    # 16진수
    print(int(X[2:], 16))
elif X.startswith("0"):
    # 8진수
    print(int(X[1:], 8))
else:
    # 10진수
    print(int(X))