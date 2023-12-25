def average(array):
    # your code goes here
    s = set(array)
    total = sum(s)
    avg = total/len(s)
    return "{:.3f}".format(avg)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)