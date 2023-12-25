n = int(input())
english_roll_numbers = list(map(int, input().split()))
b = int(input())
french_roll_numbers = list(map(int, input().split()))

s = set(english_roll_numbers)
for i in french_roll_numbers:
    s.add(i)

print(len(s))
