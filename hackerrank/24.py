from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

values = product(A, B)
for x in values:
    print(x, end=" ")