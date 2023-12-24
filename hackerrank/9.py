a = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name, score])

print(sorted(iterable = a,key = lambda a: a[1]))