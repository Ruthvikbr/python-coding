a = [10, 20, 30, 40, 5]
n = len(a)
prefix_sum = [0 for x in range(0, n)]

prefix_sum[0] = a[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

print(prefix_sum)
