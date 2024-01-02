from itertools import combinations
from collections import defaultdict


def findStudentPairs(enrollments):
    studentSet = set()
    studentDirectory = defaultdict(list)
    for i in enrollments:
        studentSet.add(i[0])
        studentDirectory[i[1]].append(i[0])

    p = combinations(studentSet, 2)
    output = defaultdict(list)
    for i, v in p:
        for courses in studentDirectory:
            if i in studentDirectory[courses] and v in studentDirectory[courses]:
                output[(i, v)].append(courses)
            elif (i, v) not in output:
                output[(i, v)] = []

    return output


enrollments1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

print(findStudentPairs(enrollments1))
