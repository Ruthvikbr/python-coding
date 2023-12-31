def encode(strs):
    return "".join(str(len(x)) + "#" + x for x in strs)


def decode(str):
    res, i = [], 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        res.append(str[j+1:j+1+length])
        i = j+1+length

    return res

print(decode(encode(["neet", "code"])))
