s = input()
k = [i for i in s if i.isalnum()]
print(len(k) > 0)
x = [i for i in s if i.isalpha()]
print(len(x) > 0)
y = [i for i in s if i.isdigit()]
print(len(y) > 0)
z = [i for i in s if i.islower()]
print(len(z) > 0)
w = [i for i in s if i.isupper()]
print(len(w) > 0)
