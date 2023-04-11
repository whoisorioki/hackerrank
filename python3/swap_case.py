def swap_case(s):
    swap = ''
    for char in s:
        if char.isupper():
            char = char.lower()
            swap += char
        elif char.islower():
            char = char.upper()
            swap += char
        else:
            swap += char
    return swap

    # return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)