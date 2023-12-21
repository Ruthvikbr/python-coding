squares = [x ** 2 for x in range(9)]
print(squares)

'''
First part is the operation on each element of the list
Second part is the loop condition that generates each item
Last part can be a conditional statement
'''

even = [x for x in range(100) if x % 2 == 0]
print(even)

'''
If you want to add an else condition move it before the for loop
'''

odd = [x if x % 2 != 0 else 0 for x in range(100)]
print(odd)
