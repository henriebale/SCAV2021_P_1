def encode(bytes):
    out = ""
    i = 0

    while (i <= len(bytes) - 1):
        count = 1
        ch = bytes[i]
        j = i
        while (j < len(bytes) - 1):
            if (bytes[j] == bytes[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        out = out + str(count) + ch
        i = j + 1
    return out


    input = input()
    encoded_message = encode(input)
    print(encoded_message)
