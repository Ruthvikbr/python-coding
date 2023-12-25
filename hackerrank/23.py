def print_formatted(number):
    # your code goes here
    n = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f"{i:>{n}} {i:>{n}o} {i:>{n}X} {i:>{n}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)