n, m = map(int, input().split())

a = list(map(int, input().split()))

A = set()
B = set()

list_a = map(int, input().split())
list_b = map(int, input().split())

A = set(list_a)
B = set(list_b)

happiness = 0

for i in range(n):
    if a[i] in A:
        happiness+=1
    if a[i] in B:
        happiness-=1

print(happiness)