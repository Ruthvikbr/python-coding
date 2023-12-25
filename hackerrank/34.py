n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    command = input()

    if 'pop' in command:
        s.pop()
    else:
        command, value = command.split()
        value = int(value)
        if command == 'remove':
            s.remove(value)
        else:
            s.discard(value)


print(sum(s))
