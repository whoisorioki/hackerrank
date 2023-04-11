def swap_case(s):
    swap = ''
    for char in s:
        if char.isupper():
            char = char.lower()
            swap += char
        elif char.islower():
            char = char.upper()
            swap += char
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)