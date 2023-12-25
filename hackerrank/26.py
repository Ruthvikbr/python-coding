from itertools import combinations

S, k = input().split()
string_list = (sorted(list(S)))
perm = []
k = int(k)
for i in range(1, k+1):
    for x in list(combinations(string_list, i)):
        perm.append(x)

for x in perm:
    print(''.join(x))
