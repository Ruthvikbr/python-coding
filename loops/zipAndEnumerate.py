letters = ['a', 'b', 'c']
nums = [1, 2, 3]

lettersAndNumbers = [('a', 1), ('b', 2), ('c', 3)]

for letter, num in zip(letters, nums):
    print(letter, num)

letter, num = zip(*lettersAndNumbers)  # unpack a tuple - returns two separate sets
print(letter, num)

letters = ['a', 'b', 'c', 'd', 'e']

for i, letter in enumerate(letters): # provides index for a list
    print(i, letter)
