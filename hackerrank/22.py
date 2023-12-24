# Enter your code here. Read input from STDIN. Print output to STDOUT
integer_list = map(int, input().split())
integer_list = list(integer_list)
n, m = integer_list[0], integer_list[1]
c = ".|."

a = []
s = "WELCOME"
char_len = 0

for i in range(n // 2):
    ch = (((2 * i) + 1) * c)
    char_len = len(ch)
    d = (m - char_len) // 2
    e = d + char_len
    count = 0
    for j in range(m):
        if d <= j < e:
            print(c[count % 3], end="")
            count += 1
        else:
            print("-", end="")
    print()

x = (m - 7) / 2
y = x + 7
count = 0

for i in range(m):
    if x <= i < y:
        print(s[count % 7], end="")
        count += 1
    else:
        print("-", end="")
print()

for i in range(n // 2):
    s = char_len - i * 2 * len(c)
    f = (m - s) // 2
    g = f + s
    count = 0
    for j in range(m):
        if f <= j < g:
            print(c[count % 3], end="")
            count += 1
        else:
            print("-", end="")
    print()