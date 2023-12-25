from collections import Counter

N = input()
shoes_list = list(input().split(' '))
shoes_list = map(int, shoes_list)
customers_count = int(input())
profit = 0

d = Counter(shoes_list)

for i in range(customers_count):
    size, price = input().split(' ')
    size = int(size)
    price = int(price)
    if size in d and d[size] != 0:
        profit += price
        d[size] = d[size]-1

print(profit)



