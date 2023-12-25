from itertools import permutations

S, k = input().split()
string_list = list(S)
perm = sorted(list(permutations(string_list, int(k))))

for x in perm:
    print(''.join(x))

