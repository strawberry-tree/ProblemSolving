import sys
input = sys.stdin.readline

A, B = input().strip().split()
rev_A = int(A[::-1])
rev_B = int(B[::-1])
print(max(rev_A, rev_B))