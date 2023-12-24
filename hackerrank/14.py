def swap_case(s):
    string_list = [x.upper() if x == x.lower() else x.lower() for x in s]
    result = ''.join(string_list)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)