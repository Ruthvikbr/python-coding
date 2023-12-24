def split_and_join(line):
    # write your code here
    string_list = line.split(' ')
    result = '-'.join(string_list)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)