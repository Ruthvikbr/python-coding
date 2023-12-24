a = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name, score])
    scores.append(score)

scores = sorted(scores)
scores= [x for x in scores if x!= min(scores)]
second_lowest = min(scores)
li = [x for [x, v] in a if v==second_lowest]

li = sorted(li)
print(*li, sep="\n")