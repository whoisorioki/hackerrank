def print_formatted(number):
    l = len('{0:b}'.format(number))
    for i in range(1, number + 1):
        decimal = '{0:}'.format(i).rjust(l)
        octal = '{0:o}'.format(i).rjust(l)
        hexadecimal = '{0:X}'.format(i).rjust(l)
        binary = '{0:b}'.format(i).rjust(l)
        print(f'{decimal} {octal} {hexadecimal} {binary}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
