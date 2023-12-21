a = [10, 12, 1, 4, 6, 8, 21]
b = []

a = sorted(a, reverse=True)

while sum(b) < 20:
    b.append(a.pop())

print(b)
