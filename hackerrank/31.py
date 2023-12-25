a_size = int(input())
a = input()
b_size = int(input())
b = input()

a_list = a.split()
b_list = b.split()

m = list(map(int, a_list))
n = list(map(int, b_list))

M = set(m)
N = set(n)

res = M.difference(N)
for i in N.difference(M):
    res.add(i)

res = sorted(res)

for x in res:
    print(x)
