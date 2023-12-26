from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

d = defaultdict(list)

for i in strs:
    val = ''.join(sorted(list(i)))
    d[val].append(i)

print(d.values())
