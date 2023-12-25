from itertools import combinations_with_replacement

S, k = input().split()
string_list = (sorted(list(S)))
k = int(k)
perm = sorted(list(combinations_with_replacement(string_list, int(k))))

for x in perm:
    print(''.join(x))