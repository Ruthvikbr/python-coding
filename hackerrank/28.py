# Complete the solve function below.
import os


def solve(s):
    result = ''
    for i in s.split(' '):
        result += i.capitalize() + ' '
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()