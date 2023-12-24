a = []
N = int(input())
for i in range(N):
    operation = input().split(' ')
    op = operation[0]
    if op == "append":
        val = int(operation[1])
        a.insert(len(a), val)
    elif op == "insert":
        val, position = int(operation[2]), int(operation[1])
        a.insert(position, val)
    elif op == "print":
        print(a)
    elif op == "remove":
        val = int(operation[1])
        a.remove(val)
    elif op == "sort":
        a.sort()
    elif op == "reverse":
        a.reverse()
    else:
        a.pop()
