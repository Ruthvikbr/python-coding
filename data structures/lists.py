list = ["a", "b", "c", 1, 2, 3]

print(list[1:3])
# b,c
print(list[-1])
# 3
print(list[0])
# a
print(list[2:])
# c,1,2,3
print(list[:3])
# a,b,c
print(list[::-1])
# 3,2,1,c,b,a
print(list[::-2])
# 3,1,b
print(list[::2])
# a,c,2
print(list[5:0:-1])
# 3,2,1,c,b

'''
Available methods for lists
1. join
2. append
3. min
4. max
5. len
6. sorted
7. pop - last element gets popped
8. in
9. not in
'''